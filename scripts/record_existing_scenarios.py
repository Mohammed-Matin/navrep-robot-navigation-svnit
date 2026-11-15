#!/usr/bin/env python
"""
Record and test all 27 existing NavRep simulation scenarios.
Runs each scenario with DWA navigation, captures video frames,
produces MP4 recordings and screenshots, and logs test results.
"""
from __future__ import print_function
import os
import sys
import json
import time
import pickle
import numpy as np
import cv2
import pyglet

import dynamic_window
from navrep.envs.ianenv import IANEnv
from navrep.envs.scenario_list import (
    scenarios, scenario_maps, rl_scenarios, rl_scenario_maps
)

OUTPUT_VIDEOS_DIR = "deliverables/existing_scenarios"
OUTPUT_SCREENSHOTS_DIR = "deliverables/screenshots/existing_scenarios"
RESULTS_FILE = "deliverables/existing_scenarios/results.json"
SCEN_DIR = os.path.expanduser(
    "~/navrep_env/lib/python3.6/site-packages/pyIA/scenarios"
)

TARGET_SIZE = (512, 512)
FPS = 20.0
MAX_STEPS_PER_SCENARIO = 150


def get_scenario_metadata(scenario_name, map_name):
    pickle_path = os.path.join(SCEN_DIR, scenario_name + ".pickle")
    if not os.path.exists(pickle_path):
        return {
            "name": scenario_name,
            "map": map_name,
            "start": [0.0, 0.0],
            "goal": [0.0, 0.0],
            "humans": 0
        }
    with open(pickle_path, "rb") as f:
        d = pickle.load(f, encoding="latin1")
    start = [round(float(x), 2) for x in d["xystates"][0]]
    goal = [round(float(x), 2) for x in d["innerstates"][0].goal]
    num_humans = len(d["agents"]) - 1
    return {
        "name": scenario_name,
        "map": map_name,
        "start": start,
        "goal": goal,
        "humans": num_humans
    }


def grab_frame(viewer):
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


def run_single_scenario(env, scenario_idx, scenario_name, map_name):
    print("\n" + "=" * 60)
    print("Running Scenario {:02d}/27: {} (Map: {})".format(
        scenario_idx, scenario_name, map_name
    ))
    print("=" * 60)

    meta = get_scenario_metadata(scenario_name, map_name)
    obs = env.reset(scenario_name)
    env.render(mode="human")

    # Paths
    vid_name_descriptive = "scenario_{:02d}_{}.mp4".format(scenario_idx, scenario_name)
    vid_name_standard = "scenario_{:02d}.mp4".format(scenario_idx)
    vid_path_descriptive = os.path.join(OUTPUT_VIDEOS_DIR, vid_name_descriptive)
    vid_path_standard = os.path.join(OUTPUT_VIDEOS_DIR, vid_name_standard)

    screenshot_path = os.path.join(
        OUTPUT_SCREENSHOTS_DIR, "{}_screenshot.png".format(scenario_name)
    )

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(vid_path_descriptive, fourcc, FPS, TARGET_SIZE)

    # Initial frame
    initial_frame = grab_frame(env._get_viewer())
    writer.write(initial_frame)
    cv2.imwrite(screenshot_path, initial_frame)

    scan, robotstate = obs
    initial_dist = float(np.hypot(robotstate[0], robotstate[1]))
    min_dist_to_goal = initial_dist
    total_reward = 0.0
    stuck_counter = 0
    goal_reached = False
    step = 0
    t_start = time.time()

    for step in range(1, MAX_STEPS_PER_SCENARIO + 1):
        gx, gy, vx, vy, vth = robotstate
        curr_dist = float(np.hypot(gx, gy))
        if curr_dist < min_dist_to_goal:
            min_dist_to_goal = curr_dist

        if curr_dist < 0.4:
            goal_reached = True
            print("  [Goal Reached] at step {}! Distance: {:.2f}m".format(step, curr_dist))
            break

        angles = np.linspace(0, 2 * np.pi, len(scan) + 1, dtype=np.float32)[:-1]

        best_u, best_v, best_score = dynamic_window.linear_dwa(
            scan.astype(np.float32), angles, vx, vy, gx, gy, 0.2,
            DV=0.05, UMIN=-0.5, UMAX=0.7, VMIN=-0.5, VMAX=0.7,
            AMAX=0.6, COMFORT_RADIUS_M=0.42
        )

        heading_err = np.arctan2(gy, gx)
        vth_cmd = float(np.clip(heading_err * 1.2, -0.8, 0.8))

        # Check for local stalling / recovery
        if abs(best_u) < 0.05 and abs(best_v) < 0.05:
            stuck_counter += 1
            if stuck_counter > 5:
                # Rotate towards goal to unstick
                vth_cmd = 0.6 if heading_err > 0 else -0.6
                best_u = 0.15
        else:
            stuck_counter = 0

        obs, rew, done, info = env.step([best_u, best_v, vth_cmd])
        scan, robotstate = obs
        total_reward += rew

        # Render & record
        env.render(mode="human")
        frame = grab_frame(env._get_viewer())
        writer.write(frame)

        if step % 25 == 0:
            print("  Step {:03d}: dist={:.2f}m, u={:.2f}, v={:.2f}, vth={:.2f}, rew={:.3f}".format(
                step, curr_dist, best_u, best_v, vth_cmd, rew
            ))

        if done:
            if info.get("goal_reached", False):
                goal_reached = True
            print("  [Done] Environment terminated at step {} (goal_reached={})".format(
                step, goal_reached
            ))
            break

    elapsed_time = time.time() - t_start
    writer.release()

    # Re-encode to high-compatibility H.264 using system ffmpeg if available
    h264_path = vid_path_descriptive.replace(".mp4", "_h264.mp4")
    ffmpeg_cmd = (
        "{}/bin/ffmpeg -y -i {} -c:v libx264 -pix_fmt yuv420p "
        "-movflags +faststart {} > /dev/null 2>&1"
    ).format(os.path.expanduser("~/navrep_env"), vid_path_descriptive, h264_path)
    if os.system(ffmpeg_cmd) == 0:
        os.replace(h264_path, vid_path_descriptive)

    # Create link or copy for standard naming
    if os.path.exists(vid_path_standard):
        os.remove(vid_path_standard)
    os.link(vid_path_descriptive, vid_path_standard)

    dist_navigated = initial_dist - min_dist_to_goal
    status = "PASS" if (goal_reached or dist_navigated > 0.5) else "FAIL"

    result = {
        "scenario_idx": scenario_idx,
        "scenario_name": scenario_name,
        "map_name": map_name,
        "start": meta["start"],
        "goal": meta["goal"],
        "humans": meta["humans"],
        "steps": step,
        "initial_dist": round(initial_dist, 2),
        "min_dist": round(min_dist_to_goal, 2),
        "dist_navigated": round(dist_navigated, 2),
        "goal_reached": goal_reached,
        "total_reward": round(total_reward, 3),
        "elapsed_sec": round(elapsed_time, 2),
        "video_path": vid_path_descriptive,
        "video_standard": vid_path_standard,
        "screenshot_path": screenshot_path,
        "status": status
    }

    print("  Outcome: {} | Steps: {} | Dist Nav: {:.2f}m | Status: {}".format(
        "Goal Reached" if goal_reached else "Navigated",
        step, dist_navigated, status
    ))
    return result


def main():
    os.makedirs(OUTPUT_VIDEOS_DIR, exist_ok=True)
    os.makedirs(OUTPUT_SCREENSHOTS_DIR, exist_ok=True)

    # Collect unique scenario names in order
    all_scenarios = []
    seen = set()
    for s, m in zip(scenarios + rl_scenarios, scenario_maps + rl_scenario_maps):
        if s not in seen:
            seen.add(s)
            all_scenarios.append((s, m))

    print("Found {} unique existing scenarios to execute and record.".format(
        len(all_scenarios)
    ))

    env = IANEnv(silent=True)
    results = []

    for idx, (scen_name, map_name) in enumerate(all_scenarios, 1):
        try:
            res = run_single_scenario(env, idx, scen_name, map_name)
            results.append(res)
        except Exception as e:
            print("ERROR in scenario {}: {}".format(scen_name, e))
            results.append({
                "scenario_idx": idx,
                "scenario_name": scen_name,
                "map_name": map_name,
                "status": "FAIL",
                "error": str(e)
            })

    env.close()

    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=2)

    print("\n" + "=" * 80)
    print("EXISTING SCENARIOS EXECUTION & RECORDING SUMMARY")
    print("=" * 80)
    print("{:<4} {:<22} {:<16} {:<12} {:<12} {:<8} {:<8}".format(
        "#", "Scenario", "Map", "Start", "Goal", "Steps", "Status"
    ))
    print("-" * 80)
    passed = 0
    for r in results:
        if r.get("status") == "PASS":
            passed += 1
        print("{:<4} {:<22} {:<16} {:<12} {:<12} {:<8} {:<8}".format(
            r.get("scenario_idx", 0),
            r.get("scenario_name", "unknown"),
            r.get("map_name", "unknown"),
            str(r.get("start", "-")),
            str(r.get("goal", "-")),
            r.get("steps", 0),
            r.get("status", "FAIL")
        ))
    print("-" * 80)
    print("TOTAL: {}/{} SCENARIOS PASSED".format(passed, len(results)))
    print("Results written to:", RESULTS_FILE)


if __name__ == "__main__":
    main()
