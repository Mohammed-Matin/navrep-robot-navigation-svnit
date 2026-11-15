#!/usr/bin/env python
"""
Builder script to generate scenario pickle files for custom NavRep scenarios:
1. Hospital Assistance Robot
2. Warehouse Navigation Robot
3. Shopping Mall Assistance Robot
"""
import os
import pickle
from pyIA import agents

def make_agent_state(start_xy, goal_xy, agent_type=agents.Person, radius=0.3):
    agent = agent_type()
    agent.radius = radius
    inner = agents.Innerstate()
    inner.goal = [float(goal_xy[0]), float(goal_xy[1])]
    inner.patience = 1
    inner.permissivity = 0.5
    inner.perceptivity = 0.9
    return agent, list(start_xy), inner, [0.0, 0.0]


def build_hospital_scenario(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pickle_path = os.path.join(output_dir, "hospital.pickle")

    # Robot: Dispensary [-8.5, -9.0] -> Care Ward [3.5, 3.5]
    robot_agent, robot_xy, robot_inner, robot_uv = make_agent_state(
        [-8.5, -9.0], [3.5, 3.5], agent_type=agents.Robot, radius=0.3
    )

    human_configs = [
        ([-5.0, -9.0], [-10.0, -9.0]),   # Doctor 1 in corridor
        ([-8.5, -5.0], [-8.5, -11.0]),   # Nurse 1 at crossing
        ([-2.0, -2.5], [-8.0, -2.5]),    # Patient 1
        ([0.0, 0.0], [-5.0, -5.0]),      # Orderly 1
        ([1.0, 3.5], [4.5, 0.0]),        # Doctor 2
        ([3.0, 1.0], [0.0, 3.0]),        # Visitor 1
        ([-6.0, -7.0], [-2.0, -7.0]),    # Nurse 2
        ([-4.0, 2.0], [-4.0, -2.0]),     # Orderly 2
    ]

    all_agents = [robot_agent]
    all_xystates = [robot_xy]
    all_innerstates = [robot_inner]
    all_uvstates = [robot_uv]

    for start_xy, goal_xy in human_configs:
        ag, xy, inn, uv = make_agent_state(start_xy, goal_xy, agent_type=agents.Person, radius=0.3)
        all_agents.append(ag)
        all_xystates.append(xy)
        all_innerstates.append(inn)
        all_uvstates.append(uv)

    scenario_dict = {
        "agents": all_agents,
        "xystates": all_xystates,
        "innerstates": all_innerstates,
        "uvstates": all_uvstates,
    }

    with open(pickle_path, "wb") as f:
        pickle.dump(scenario_dict, f, protocol=2)
    print("Hospital scenario generated at:", pickle_path)
    return pickle_path


def build_warehouse_scenario(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pickle_path = os.path.join(output_dir, "warehouse.pickle")

    # Robot: Inbound Receiving [5.0, 8.0] -> Dispatch Bay [-14.0, 3.0]
    robot_agent, robot_xy, robot_inner, robot_uv = make_agent_state(
        [5.0, 8.0], [-14.0, 3.0], agent_type=agents.Robot, radius=0.35
    )

    human_configs = [
        ([3.0, 5.0], [-2.0, 5.0]),       # Picker 1
        ([0.0, 8.0], [5.0, 2.0]),        # Picker 2
        ([-5.0, 2.0], [-5.0, 8.0]),      # Forklift 1
        ([-8.0, 5.0], [-12.0, 5.0]),     # Picker 3
        ([-10.0, 1.0], [-3.0, 1.0]),     # Transporter 1
        ([-12.0, 8.0], [-8.0, 8.0]),     # Picker 4
        ([2.0, 0.0], [-4.0, 0.0]),       # Picker 5
        ([-6.0, -4.0], [-12.0, 0.0]),    # Transporter 2
        ([-2.0, 7.0], [-2.0, 2.0]),      # Inventory Checker
        ([-14.0, 7.0], [-10.0, 3.0]),    # Pallet Loader
    ]

    all_agents = [robot_agent]
    all_xystates = [robot_xy]
    all_innerstates = [robot_inner]
    all_uvstates = [robot_uv]

    for start_xy, goal_xy in human_configs:
        ag, xy, inn, uv = make_agent_state(start_xy, goal_xy, agent_type=agents.Person, radius=0.35)
        all_agents.append(ag)
        all_xystates.append(xy)
        all_innerstates.append(inn)
        all_uvstates.append(uv)

    scenario_dict = {
        "agents": all_agents,
        "xystates": all_xystates,
        "innerstates": all_innerstates,
        "uvstates": all_uvstates,
    }

    with open(pickle_path, "wb") as f:
        pickle.dump(scenario_dict, f, protocol=2)
    print("Warehouse scenario generated at:", pickle_path)
    return pickle_path


def build_shopping_mall_scenario(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pickle_path = os.path.join(output_dir, "shopping_mall.pickle")

    # Robot: Mall Welcome Desk [-4.0, -1.5] -> Department Store [5.5, -0.5]
    robot_agent, robot_xy, robot_inner, robot_uv = make_agent_state(
        [-4.0, -1.5], [5.5, -0.5], agent_type=agents.Robot, radius=0.3
    )

    human_configs = [
        ([-2.0, -0.8], [-2.0, -2.2]),    # Crossing Shopper 1
        ([0.0, -2.2], [0.0, -0.8]),      # Crossing Shopper 2
        ([2.0, -0.8], [2.0, -2.2]),      # Crossing Shopper 3
        ([4.0, -2.2], [4.0, -0.8]),      # Crossing Shopper 4
        ([-1.0, -1.5], [-3.5, -1.5]),    # Oncoming Shopper 5
        ([3.5, -1.2], [1.0, -1.2]),      # Oncoming Shopper 6
        ([1.0, -2.0], [3.0, -0.8]),      # Diagonal Shopper 7
        ([-3.0, -0.8], [-1.0, -2.2]),    # Diagonal Shopper 8
    ]

    all_agents = [robot_agent]
    all_xystates = [robot_xy]
    all_innerstates = [robot_inner]
    all_uvstates = [robot_uv]

    for start_xy, goal_xy in human_configs:
        ag, xy, inn, uv = make_agent_state(start_xy, goal_xy, agent_type=agents.Person, radius=0.3)
        all_agents.append(ag)
        all_xystates.append(xy)
        all_innerstates.append(inn)
        all_uvstates.append(uv)

    scenario_dict = {
        "agents": all_agents,
        "xystates": all_xystates,
        "innerstates": all_innerstates,
        "uvstates": all_uvstates,
    }

    with open(pickle_path, "wb") as f:
        pickle.dump(scenario_dict, f, protocol=2)
    print("Shopping Mall scenario generated at:", pickle_path)
    return pickle_path


if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.dirname(__file__))
    build_hospital_scenario(os.path.join(base_dir, "hospital"))
    build_warehouse_scenario(os.path.join(base_dir, "warehouse"))
    build_shopping_mall_scenario(os.path.join(base_dir, "shopping_mall"))
