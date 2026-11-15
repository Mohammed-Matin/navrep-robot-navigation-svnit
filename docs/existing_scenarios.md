# Existing NavRep Simulation Scenarios: Comprehensive Analysis & Inventory

**Course**: CS359 – Artificial Intelligence for Robotics  
**Institution**: Sardar Vallabhbhai National Institute of Technology (SVNIT), Surat  
**Department**: Department of Computer Science and Engineering  
**Project**: NavRep – Robot Navigation and Simulation  

---

## 1. Executive Summary & Inventory Overview

A systematic inspection of the ETH Zurich NavRep codebase reveals that simulation scenarios are defined across two primary environment families:
1. **Interactive Agent Environments (`pyIA` / `IANEnv`)**: Defined in `navrep/envs/scenario_list.py` and backed by serialized environment states in `pyIA/scenarios/*.pickle`. There are **27 benchmark scenarios** in total:
   - **18 IROS Benchmark Scenarios**: Real-world evaluation scenarios spanning dense pedestrian crowds, long hallways, and multi-obstacle layouts.
   - **9 Reinforcement Learning Curriculum Scenarios**: Progressive difficulty stages (`rlasl`, `rlasl_office_j`, `rlunity_scene_map`) designed for policy training and transfer testing.
2. **Procedural Training Environments (`NavRepTrainEnv`)**: Parameterized simulation environments featuring procedural crowd generation (0 to 5 dynamic humans) and procedural static obstacles (up to 10 randomly generated walls and circular columns).

Below is the complete inventory of all 27 identified simulation scenarios.

---

## 2. Complete Inventory Table of All 27 Scenarios

| # | Scenario Name | Map Name | Start Position $[x, y]$ | Goal Position $[x, y]$ | Initial Dist (m) | Dynamic Humans | Scenario Description |
| :- | :--- | :--- | :--- | :--- | :-: | :-: | :--- |
| **01** | `irosasl1` | `asl` | `[1.30, -2.62]` | `[-6.65, -2.64]` | 7.95 | 26 | Extremely dense pedestrian crowd crossing corridor between robot start and goal. |
| **02** | `irosasl2` | `asl` | `[-10.36, -10.03]` | `[5.12, 5.02]` | 21.60 | 0 | Long-range diagonal static wall traversal across the entire ASL laboratory floor. |
| **03** | `irosasl3` | `asl` | `[-9.30, -11.24]` | `[5.17, 5.24]` | 21.93 | 19 | Cross-floor navigation with multiple pedestrian clusters and crossing groups. |
| **04** | `irosasl4` | `asl` | `[4.96, -6.51]` | `[5.04, 1.60]` | 8.11 | 8 | Northward transit along vertical corridor with intersecting pedestrian paths. |
| **05** | `irosasl5` | `asl` | `[-6.31, -11.43]` | `[-6.43, 6.29]` | 17.72 | 9 | Straight-line corridor traversal past multiple doorway openings and pedestrians. |
| **06** | `irosasl6` | `asl` | `[-9.30, -11.24]` | `[5.17, 5.24]` | 21.93 | 9 | Diagonal transit with sparse crossing humans requiring high-speed path adjustment. |
| **07** | `irosasl_office_j1` | `asl_office_j` | `[-21.41, -4.02]` | `[-24.37, 3.23]` | 7.83 | 15 | West office wing corridor with high-density personnel movement. |
| **08** | `irosasl_office_j2` | `asl_office_j` | `[-21.53, -3.50]` | `[13.51, 7.39]` | 36.70 | 0 | Full-facility west-to-east traversal across office corridors without pedestrians. |
| **09** | `irosasl_office_j3` | `asl_office_j` | `[5.06, -1.09]` | `[-2.87, 6.11]` | 10.72 | 10 | Central atrium transit with dynamic personnel moving between cubicles. |
| **10** | `irosasl_office_j4` | `asl_office_j` | `[-3.55, -1.53]` | `[5.42, -0.57]` | 9.02 | 8 | Main hallway east-west navigation with oncoming and passing pedestrians. |
| **11** | `irosasl_office_j5` | `asl_office_j` | `[-22.69, -3.98]` | `[1.18, -1.05]` | 24.05 | 7 | Long hallway approach from office annex to central meeting space. |
| **12** | `irosasl_office_j6` | `asl_office_j` | `[-21.65, -3.33]` | `[13.81, 7.07]` | 36.95 | 6 | End-to-end office transit past moving personnel and room doorways. |
| **13** | `irosunity_scene_map1` | `unity_scene_map` | `[5.16, 9.35]` | `[-4.12, 9.57]` | 9.28 | 17 | Warehouse cross-aisle navigation amidst dense order picking personnel. |
| **14** | `irosunity_scene_map2` | `unity_scene_map` | `[1.03, -8.80]` | `[-17.44, 5.50]` | 23.35 | 0 | Static logistics rack perimeter traversal without dynamic agents. |
| **15** | `irosunity_scene_map3` | `unity_scene_map` | `[3.67, 8.65]` | `[5.64, -8.55]` | 17.31 | 17 | High-traffic vertical warehouse corridor with multiple crossing pickers. |
| **16** | `irosunity_scene_map4` | `unity_scene_map` | `[-0.07, 0.27]` | `[-16.96, 0.40]` | 16.89 | 8 | Cross-dock logistics transfer through central warehouse corridor. |
| **17** | `irosunity_scene_map5` | `unity_scene_map` | `[-3.69, -8.23]` | `[-3.53, 9.11]` | 17.34 | 7 | North-south storage bay navigation yielding to moving pallet transporters. |
| **18** | `irosunity_scene_map6` | `unity_scene_map` | `[5.01, -0.26]` | `[-17.99, -0.23]` | 23.00 | 14 | East-west horizontal thoroughfare traversing multiple storage bays. |
| **19** | `rlasl1` | `asl` | `[-3.93, -4.14]` | `[-1.23, -1.29]` | 3.93 | 0 | Curriculum Stage 1 (ASL): Short-range open-space goal navigation. |
| **20** | `rlasl2` | `asl` | `[-8.39, -4.93]` | `[-7.11, -8.08]` | 3.40 | 0 | Curriculum Stage 2 (ASL): Medium-distance static corridor turn navigation. |
| **21** | `rlasl3` | `asl` | `[-0.20, -1.88]` | `[-3.44, -3.35]` | 3.56 | 9 | Curriculum Stage 3 (ASL): Dynamic crowd avoidance in central ASL area. |
| **22** | `rlasl_office_j1` | `asl_office_j` | `[-21.03, -3.95]` | `[-21.76, -1.34]` | 2.71 | 0 | Curriculum Stage 1 (Office): Direct short corridor target navigation. |
| **23** | `rlasl_office_j2` | `asl_office_j` | `[-22.79, -0.26]` | `[-22.67, 3.38]` | 3.64 | 0 | Curriculum Stage 2 (Office): Medium hallway navigation around wall corner. |
| **24** | `rlasl_office_j3` | `asl_office_j` | `[-21.05, -4.30]` | `[-21.22, -2.08]` | 2.23 | 7 | Curriculum Stage 3 (Office): Dynamic personnel avoidance at hallway intersection. |
| **25** | `rlunity_scene_map1` | `unity_scene_map` | `[2.88, 0.41]` | `[-0.91, 0.30]` | 3.79 | 0 | Curriculum Stage 1 (Unity): Short-range open-bay navigation. |
| **26** | `rlunity_scene_map2` | `unity_scene_map` | `[0.62, 1.39]` | `[1.11, 5.25]` | 3.89 | 0 | Curriculum Stage 2 (Unity): Mid-range navigation along warehouse shelf rack. |
| **27** | `rlunity_scene_map3` | `unity_scene_map` | `[4.51, 1.90]` | `[1.44, -0.63]` | 3.99 | 9 | Curriculum Stage 3 (Unity): Dynamic warehouse worker avoidance in storage aisle. |

---

## 3. Environment Map Breakdown

### 3.1 ETH Zurich Autonomous Systems Lab (`asl`)
- **Map File**: `asl.yaml` / `asl.pgm` (Resolution: 0.16 m/cell, Origin: `[-12.8, -12.8]`)
- **Environment Context**: Research robotics laboratory floor plan with interconnected office suites, central robotic testing arena, and partitioned workspaces.
- **Scenarios Hosted**: 9 scenarios (`irosasl1`–`irosasl6`, `rlasl1`–`rlasl3`).

### 3.2 Office Complex Layout (`asl_office_j`)
- **Map File**: `asl_office_j.yaml` / `asl_office_j.pgm` (Resolution: 0.16 m/cell, Origin: `[-25.6, -12.8]`)
- **Environment Context**: Large corporate office environment featuring long primary corridors, rectangular cubicle groupings, conference spaces, and narrow office doorways.
- **Scenarios Hosted**: 9 scenarios (`irosasl_office_j1`–`irosasl_office_j6`, `rlasl_office_j1`–`rlasl_office_j3`).

### 3.3 Unity Industrial Logistics Scene (`unity_scene_map`)
- **Map File**: `unity_scene_map.yaml` / `unity_scene_map.pgm` (Resolution: 0.16 m/cell, Origin: `[-20.48, -12.8]`)
- **Environment Context**: High-density fulfillment warehouse with repetitive parallel racking aisles, packing stations, cross-dock loading areas, and industrial partition walls.
- **Scenarios Hosted**: 9 scenarios (`irosunity_scene_map1`–`irosunity_scene_map6`, `rlunity_scene_map1`–`rlunity_scene_map3`).

---

## 4. Robot & Sensor Configuration

Across all existing scenarios:
- **Kinematics**: Differential drive / holonomic 2D planar motion model.
- **Robot Footprint**: Circular footprint with radius $r = 0.30\text{ m}$.
- **LiDAR Sensor**: 360° planar range scanner with 1080 angular rays covering $[0, 2\pi]$ radians at 25.0 m maximum range.
- **State Feedback**: Relative goal vector $(g_x, g_y)$ in robot coordinate frame and instantaneous velocities $(v_x, v_y, \omega)$.
- **Local Navigation Controller**: Dynamic Window Approach (DWA) in C++ Cython with forward speed up to $0.70\text{ m/s}$ and rotational correction up to $0.80\text{ rad/s}$.

---

## 5. Execution Instructions

To execute all 27 existing scenarios and generate video recordings:
```bash
./run.sh python scripts/record_existing_scenarios.py
```

All generated video recordings are saved to `deliverables/existing_scenarios/` and indexed in `deliverables/video_index.md`.
