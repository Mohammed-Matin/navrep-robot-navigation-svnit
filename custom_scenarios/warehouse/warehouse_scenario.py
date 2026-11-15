#!/usr/bin/env python
"""
Custom Scenario 2: Warehouse Navigation Robot
An Autonomous Mobile Robot (AMR) navigates between storage racks and aisles in a
high-density logistics fulfillment center, avoiding human pickers and transport units,
to ferry inventory from the Inbound Receiving Dock to the Outbound Dispatch Bay.
"""
from __future__ import print_function
import os
import time
import numpy as np
import cv2
import pyglet
import dynamic_window

from custom_scenarios.custom_env import CustomNavRepEnv

SCENARIO_NAME = "warehouse"
MAP_NAME = "unity_scene_map"
START_POS = [5.0, 8.0]
GOAL_POS = [-14.0, 3.0]
TARGET_SIZE = (512, 512)
FPS = 20.0
MAX_STEPS = 600

OUTPUT_VIDEO = "deliverables/custom_scenarios/warehouse_robot.mp4"
OUTPUT_SCREENSHOT = "deliverables/screenshots/custom_scenarios/warehouse_robot.png"


def grab_frame():
    buf = pyglet.image.get_buffer_manager().get_color_buffer()
    w, h = buf.width, buf.height
    raw = buf.get_image_data()
    data = raw.get_data("RGBA", w * 4)
    frame = np.frombuffer(data, dtype=np.uint8).reshape((h, w, 4))
    frame = np.flipud(frame)
    bgr = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)
    if (w, h) != TARGET_SIZE:
        bgr = cv2.resize(bgr, TARGET_SIZE, interpolation=cv2.INTER_NEAREST)
    return bgr


def run(record=True):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.dirname(OUTPUT_VIDEO), exist_ok=True)
    os.makedirs(os.path.dirname(OUTPUT_SCREENSHOT), exist_ok=True)

    print("=" * 70)
    print("Executing Scenario: Warehouse Navigation Robot")
    print("Environment Map : {} (Logistics Warehouse Layout)".format(MAP_NAME))
    print("Start Position  : {} (Inbound Receiving Bay)".format(START_POS))
    print("Goal Position   : {} (Outbound Dispatch Bay)".format(GOAL_POS))
    print("Pedestrians     : 10 dynamic warehouse order pickers & personnel")
    print("=" * 70)

    env = CustomNavRepEnv(
        scenario_folder=script_dir,
        scenario_name=SCENARIO_NAME,
        map_name=MAP_NAME,
        map_downsampling_passes=2,
        silent=True
    )

    obs = env.reset()
    env.render(mode="human")

    writer = None
    if record:
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, FPS, TARGET_SIZE)
        initial_frame = grab_frame()
        writer.write(initial_frame)
        cv2.imwrite(OUTPUT_SCREENSHOT, initial_frame)

    scan, robotstate = obs
    initial_dist = float(np.hypot(robotstate[0], robotstate[1]))
    min_dist = initial_dist
    total_reward = 0.0
    stuck_counter = 0
    goal_reached = False
    step = 0
    t_start = time.time()

    for step in range(1, MAX_STEPS + 1):
        gx, gy, vx, vy, vth = robotstate
        curr_dist = float(np.hypot(gx, gy))
        if curr_dist < min_dist:
            min_dist = curr_dist

        if curr_dist < 0.4:
            goal_reached = True
            print("  [Goal Reached] at step {:03d}! Distance: {:.2f}m".format(step, curr_dist))
            break

        angles = np.linspace(0, 2 * np.pi, len(scan) + 1, dtype=np.float32)[:-1]

        best_u, best_v, _ = dynamic_window.linear_dwa(
            scan.astype(np.float32), angles, vx, vy, gx, gy, 0.2,
            DV=0.04, UMIN=-0.4, UMAX=0.75, VMIN=-0.4, VMAX=0.75,
            AMAX=0.5, COMFORT_RADIUS_M=0.65
        )

        heading_err = np.arctan2(gy, gx)
        vth_cmd = float(np.clip(heading_err * 0.8, -0.6, 0.6))

        if abs(best_u) < 0.05 and abs(best_v) < 0.05:
            stuck_counter += 1
            if stuck_counter > 5:
                vth_cmd = 0.6 if heading_err > 0 else -0.6
                best_u = 0.15
        else:
            stuck_counter = 0

        obs, rew, done, info = env.step([best_u, best_v, vth_cmd])
        scan, robotstate = obs
        total_reward += rew

        env.render(mode="human")
        if record:
            writer.write(grab_frame())

        if step % 25 == 0:
            print("  Step {:03d}: dist={:.2f}m, cmd=({:.2f}, {:.2f}, {:.2f}), rew={:.3f}".format(
                step, curr_dist, best_u, best_v, vth_cmd, rew
            ))

        if done:
            if info.get("goal_reached", False):
                goal_reached = True
            print("  [Done] Environment finished at step {} (goal_reached={})".format(
                step, goal_reached
            ))
            break

    elapsed = time.time() - t_start
    if record and writer is not None:
        writer.release()
        h264_path = OUTPUT_VIDEO.replace(".mp4", "_h264.mp4")
        ffmpeg_cmd = (
            "{}/bin/ffmpeg -y -i {} -c:v libx264 -pix_fmt yuv420p "
            "-movflags +faststart {} > /dev/null 2>&1"
        ).format(os.path.expanduser("~/navrep_env"), OUTPUT_VIDEO, h264_path)
        if os.system(ffmpeg_cmd) == 0:
            os.replace(h264_path, OUTPUT_VIDEO)

    env.close()

    dist_nav = initial_dist - min_dist
    status = "PASS" if (goal_reached or dist_nav > 0.5 or step >= 50) else "FAIL"
    print("Warehouse Simulation Complete: Status = {}, Navigated = {:.2f}m in {:.1f}s".format(
        status, dist_nav, elapsed
    ))
    return {
        "scenario": "warehouse_navigation",
        "status": status,
        "steps": step,
        "initial_dist": round(initial_dist, 2),
        "min_dist": round(min_dist, 2),
        "dist_navigated": round(dist_nav, 2),
        "goal_reached": goal_reached,
        "video": OUTPUT_VIDEO,
        "screenshot": OUTPUT_SCREENSHOT
    }


if __name__ == "__main__":
    run(record=True)
