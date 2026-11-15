# NavRep – Autonomous Robot Navigation and Simulation

**Course**: CS359 – Artificial Intelligence for Robotics  
**Institution**: Sardar Vallabhbhai National Institute of Technology (SVNIT), Surat  
**Department**: Department of Computer Science and Engineering  
**Student Contributor**: Mohammed Matin  
**GitHub Repository**: [navrep-robot-navigation-svnit](https://github.com/Mohammed-Matin/navrep-robot-navigation-svnit)  
**Upstream Reference**: [ethz-asl/navrep](https://github.com/ethz-asl/navrep) by Autonomous Systems Lab (ASL), ETH Zurich  

---

## 1. Project Introduction

NavRep is an open-source robotic navigation and simulation framework developed by the Autonomous Systems Lab (ASL) at ETH Zurich. It evaluates deep reinforcement learning (RL) policies, world models (e.g. VAEs, RNNs, GPT, Transformer architectures), and classical local navigation planners (such as the Dynamic Window Approach) on simulated planar mobile robots navigating through complex, dynamic indoor environments with moving pedestrians and static obstacles.

This repository serves as the complete, reproducible submission for the SVNIT CS359 Artificial Intelligence for Robotics project assignment. It contains:
- The verified, fully configured ETH Zurich NavRep core and its C++/Cython extensions.
- An automated, isolated runtime environment for modern Linux distributions.
- Comprehensive evaluation and recorded video evidence for **all 27 existing benchmark scenarios**.
- Implementation, validation, and video evidence for **three original custom simulation scenarios** (Hospital Assistance Robot, Warehouse Navigation Robot, Shopping Mall Assistance Robot).
- Complete technical documentation, test matrices, and reproducibility scripts.

---

## 2. Project Objectives

1. **Environment Setup & Compatibility**: Build a completely isolated, reproducible Python 3.6 environment with required legacy robotics libraries (Gym 0.15.7, TensorFlow 1.13.2, Keras 2.3.1, Stable-Baselines 2.10.0, PyTorch 1.6.0 CPU, ROS 1 Python bindings) on modern Ubuntu 22.04 LTS without damaging host system packages.
2. **Existing Scenario Evaluation**: Identify, execute, validate, and record simulation videos for every existing simulation scenario in the official repository.
3. **Custom Scenario Development**: Design and implement at least three original simulation scenarios modifying robot start positions, goal destinations, environment layouts, and pedestrian movement dynamics.
4. **Autonomous Navigation**: Deploy and tune real-time obstacle avoidance and goal navigation (C++ Dynamic Window Approach) to achieve smooth, collision-free robot guidance.
5. **Quality Assurance & Deliverables**: Document full installation steps, scenario inventories, test results, video indices, and package the project into a submission archive.

---

## 3. Original NavRep Repository Reference

- **Upstream Repository**: [https://github.com/ethz-asl/navrep](https://github.com/ethz-asl/navrep)
- **Primary Authors**: Daniel Dugas et al., ETH Zurich Autonomous Systems Lab (ASL)
- **License**: MIT License (Preserved in full; see [LICENSE_AND_ATTRIBUTION.md](file:///home/matin/laboratery/AIR/air_project/LICENSE_AND_ATTRIBUTION.md))

---

## 4. System Specifications & Compatibility

The deployment has been validated on the following host environment:

| Property | Value |
| :--- | :--- |
| **Operating System** | Ubuntu 22.04.5 LTS (Linux kernel 6.6.87.2-microsoft-standard-WSL2) |
| **Architecture** | x86_64 (Intel Core i5-11400H @ 2.70 GHz, 4 vCPUs allocated) |
| **System Memory** | 3.7 GiB Virtual RAM + 8.0 GiB Swap |
| **Graphics / Display** | WSLg Wayland/X11 Virtual Server (`DISPLAY=:0`) |
| **Rendering Backend** | Pyglet 1.5.22 OpenGL Backbuffer capture |
| **Video Encoding** | FFmpeg 7.0.2 with `libx264` (H.264 High Profile, YUV420p) |

---

## 5. Software Requirements & Dependency Versions

Key pinned software packages configured in `requirements-pinned.txt`:

| Package | Version | Purpose |
| :--- | :--- | :--- |
| `python` | `3.6.15` | Target Python runtime required by NavRep |
| `numpy` | `1.19.5` | Pinned C-ABI numeric computation backend |
| `Cython` | `0.29.28` | C/C++ extension compiler for `crings`, `lib_dwa`, `lib_clustering` |
| `gym` | `0.15.7` | Standard RL environment interface |
| `tensorflow` | `1.13.2` | Deep learning backend for legacy policies |
| `keras` | `2.3.1` | High-level neural network specification |
| `stable-baselines` | `2.10.0` | Reinforcement learning algorithms (PPO2) |
| `torch` | `1.6.0+cpu` | PyTorch backend for transformer/GPT models |
| `pyglet` | `1.5.22` | Simulation viewer and OpenGL rendering engine |
| `opencv-python` | `4.5.5.64` | Computer vision, frame processing, video encoding |
| `asl-pepper-2d-sim` | `0.0.5` | ETH Zurich Pepper 2D planar robot simulator |
| `pyIAN` | `0.0.3` | Interactive Agent Navigation benchmark engine |
| `pyrangelibc-danieldugas` | `0.0.2` | Fast GPU/CPU 2D LiDAR raycasting |
| `pyrvo2-danieldugas` | `0.0.2` | Reciprocal Velocity Obstacles for pedestrian crowds |
| `rospy` / `sensor-msgs` | ROS 1 Melodic | Pure-Python ROS 1 communication via rospypi |

---

## 6. Virtual Environment Creation & Installation

### Quick Automated Installation
To set up the entire isolated environment and compile all extensions automatically:
```bash
chmod +x setup.sh run.sh
./setup.sh
```

### Script Execution Wrapper (`./run.sh`)
The provided `./run.sh` script guarantees execution inside the isolated `~/navrep_env` prefix without polluting host environments:
```bash
./run.sh python --version
# Output: Python 3.6.15
```

For complete manual step-by-step commands, refer to [docs/installation.md](file:///home/matin/laboratery/AIR/air_project/docs/installation.md).

---

## 7. Repository Structure

```
navrep-robot-navigation-svnit/
├── setup.sh                     # Idempotent environment installer
├── run.sh                       # Isolated execution wrapper
├── requirements-pinned.txt       # Exact pinned package dependencies
├── LICENSE                      # Original MIT License
├── LICENSE_AND_ATTRIBUTION.md   # Academic and upstream attribution notice
├── README.md                    # Project documentation
│
├── navrep/                      # Core NavRep framework
│   ├── envs/                    # Environment wrappers (IANEnv, NavRepTrainEnv, etc.)
│   ├── models/                  # VAE, RNN, GPT, and custom policies
│   ├── scripts/                 # Official training and evaluation scripts
│   └── tools/                   # Rendering, dataset, and player utilities
│
├── custom_scenarios/            # Original Custom Simulation Scenarios
│   ├── custom_env.py            # Reusable environment loader for custom scenarios
│   ├── scenario_builder.py      # Automated pickle scenario generator
│   ├── run_all.py               # Runner for all custom scenarios
│   ├── hospital/                # Hospital Assistance Robot
│   ├── warehouse/               # Warehouse Navigation Robot
│   └── shopping_mall/           # Shopping Mall Assistance Robot
│
├── scripts/
│   └── record_existing_scenarios.py # Systematic runner for all 27 benchmark scenarios
│
├── docs/                        # In-depth technical reports
│   ├── installation.md          # Environment setup guide
│   ├── existing_scenarios.md    # Inventory of all 27 existing scenarios
│   ├── custom_scenarios.md      # Custom scenario specifications & analysis
│   └── testing_report.md        # Formal test matrix & verification logs
│
├── deliverables/                # Generated simulation videos & screenshots
│   ├── video_index.md           # Registry of all recorded MP4 videos
│   ├── existing_scenarios/      # Recordings of all 27 benchmark scenarios
│   ├── custom_scenarios/        # Recordings of the 3 custom scenarios
│   └── screenshots/             # High-resolution simulation screenshots
│
└── external/                    # Local C++/Cython extensions
    ├── lib_clustering/          # Point cloud clustering extension
    ├── lib_dwa/                 # Dynamic Window Approach local planner
    ├── frame_msgs/              # ROS coordinate frame message definitions
    └── tf_bag/                  # ROS bag transformation extractor
```

---

## 8. Instructions to Execute NavRep

### Basic Simulator Smoke Test
```bash
./run.sh python -c "
from navrep.envs.ianenv import IANEnv
env = IANEnv(silent=True)
obs = env.reset('rlasl1')
print('Obs shape:', [o.shape for o in obs])
obs, rew, done, info = env.step([0.2, 0.0, 0.0])
print('Step succeeded, reward:', rew)
env.close()
"
```

### Interactive Manual Driving
Drive the simulated robot interactively using keyboard controls (WASD to steer):
```bash
./run.sh python -m navrep.scripts.play_ianenv
```

---

## 9. Existing Scenario Execution & Results

NavRep defines **27 benchmark simulation scenarios** spanning three distinct environments:
- **`asl`**: ETH Zurich Autonomous Systems Lab research floor
- **`asl_office_j`**: Expansive corporate office complex
- **`unity_scene_map`**: Industrial logistics warehouse

### Running All Existing Scenarios
To run and record all 27 existing scenarios automatically:
```bash
./run.sh python scripts/record_existing_scenarios.py
```

### Existing Scenarios Overview

| Scenario Name | Environment | Start $(x, y)$ | Goal $(x, y)$ | Humans | Video File | Status |
| :--- | :--- | :--- | :--- | :-: | :--- | :---: |
| `irosasl1` | `asl` | `[1.30, -2.62]` | `[-6.65, -2.64]` | 26 | `scenario_01_irosasl1.mp4` | **PASS** |
| `irosasl2` | `asl` | `[-10.36, -10.03]` | `[5.12, 5.02]` | 0 | `scenario_02_irosasl2.mp4` | **PASS** |
| `irosasl3` | `asl` | `[-9.30, -11.24]` | `[5.17, 5.24]` | 19 | `scenario_03_irosasl3.mp4` | **PASS** |
| `irosasl4` | `asl` | `[4.96, -6.51]` | `[5.04, 1.60]` | 8 | `scenario_04_irosasl4.mp4` | **PASS** |
| `irosasl5` | `asl` | `[-6.31, -11.43]` | `[-6.43, 6.29]` | 9 | `scenario_05_irosasl5.mp4` | **PASS** |
| `irosasl6` | `asl` | `[-9.30, -11.24]` | `[5.17, 5.24]` | 9 | `scenario_06_irosasl6.mp4` | **PASS** |
| `irosasl_office_j1` | `asl_office_j` | `[-21.41, -4.02]` | `[-24.37, 3.23]` | 15 | `scenario_07_irosasl_office_j1.mp4` | **PASS** |
| `irosasl_office_j2` | `asl_office_j` | `[-21.53, -3.50]` | `[13.51, 7.39]` | 0 | `scenario_08_irosasl_office_j2.mp4` | **PASS** |
| `irosasl_office_j3` | `asl_office_j` | `[5.06, -1.09]` | `[-2.87, 6.11]` | 10 | `scenario_09_irosasl_office_j3.mp4` | **PASS** |
| `irosasl_office_j4` | `asl_office_j` | `[-3.55, -1.53]` | `[5.42, -0.57]` | 8 | `scenario_10_irosasl_office_j4.mp4` | **PASS** |
| `irosasl_office_j5` | `asl_office_j` | `[-22.69, -3.98]` | `[1.18, -1.05]` | 7 | `scenario_11_irosasl_office_j5.mp4` | **PASS** |
| `irosasl_office_j6` | `asl_office_j` | `[-21.65, -3.33]` | `[13.81, 7.07]` | 6 | `scenario_12_irosasl_office_j6.mp4` | **PASS** |
| `irosunity_scene_map1` | `unity_scene_map` | `[5.16, 9.35]` | `[-4.12, 9.57]` | 17 | `scenario_13_irosunity_scene_map1.mp4` | **PASS** |
| `irosunity_scene_map2` | `unity_scene_map` | `[1.03, -8.80]` | `[-17.44, 5.50]` | 0 | `scenario_14_irosunity_scene_map2.mp4` | **PASS** |
| `irosunity_scene_map3` | `unity_scene_map` | `[3.67, 8.65]` | `[5.64, -8.55]` | 17 | `scenario_15_irosunity_scene_map3.mp4` | **PASS** |
| `irosunity_scene_map4` | `unity_scene_map` | `[-0.07, 0.27]` | `[-16.96, 0.40]` | 8 | `scenario_16_irosunity_scene_map4.mp4` | **PASS** |
| `irosunity_scene_map5` | `unity_scene_map` | `[-3.69, -8.23]` | `[-3.53, 9.11]` | 7 | `scenario_17_irosunity_scene_map5.mp4` | **PASS** |
| `irosunity_scene_map6` | `unity_scene_map` | `[5.01, -0.26]` | `[-17.99, -0.23]` | 14 | `scenario_18_irosunity_scene_map6.mp4` | **PASS** |
| `rlasl1` | `asl` | `[-3.93, -4.14]` | `[-1.23, -1.29]` | 0 | `scenario_19_rlasl1.mp4` | **PASS** |
| `rlasl2` | `asl` | `[-8.39, -4.93]` | `[-7.11, -8.08]` | 0 | `scenario_20_rlasl2.mp4` | **PASS** |
| `rlasl3` | `asl` | `[-0.20, -1.88]` | `[-3.44, -3.35]` | 9 | `scenario_21_rlasl3.mp4` | **PASS** |
| `rlasl_office_j1` | `asl_office_j` | `[-21.03, -3.95]` | `[-21.76, -1.34]` | 0 | `scenario_22_rlasl_office_j1.mp4` | **PASS** |
| `rlasl_office_j2` | `asl_office_j` | `[-22.79, -0.26]` | `[-22.67, 3.38]` | 0 | `scenario_23_rlasl_office_j2.mp4` | **PASS** |
| `rlasl_office_j3` | `asl_office_j` | `[-21.05, -4.30]` | `[-21.22, -2.08]` | 7 | `scenario_24_rlasl_office_j3.mp4` | **PASS** |
| `rlunity_scene_map1` | `unity_scene_map` | `[2.88, 0.41]` | `[-0.91, 0.30]` | 0 | `scenario_25_rlunity_scene_map1.mp4` | **PASS** |
| `rlunity_scene_map2` | `unity_scene_map` | `[0.62, 1.39]` | `[1.11, 5.25]` | 0 | `scenario_26_rlunity_scene_map2.mp4` | **PASS** |
| `rlunity_scene_map3` | `unity_scene_map` | `[4.51, 1.90]` | `[1.44, -0.63]` | 9 | `scenario_27_rlunity_scene_map3.mp4` | **PASS** |

See [docs/existing_scenarios.md](file:///home/matin/laboratery/AIR/air_project/docs/existing_scenarios.md) and [deliverables/video_index.md](file:///home/matin/laboratery/AIR/air_project/deliverables/video_index.md) for full scenario documentation.

---

## 10. Custom Scenario Development & Results

Three original simulation scenarios were created:

### Scenario 1: Hospital Assistance Robot (`custom_scenarios/hospital/`)
- **Concept**: A mobile medical assistant transports critical pharmaceuticals from the dispensary to an acute care room through narrow corridors while avoiding doctors, nurses, and moving hospital beds.
- **Map Base**: `asl` (Hospital Ward Floor)
- **Start Position**: `[-8.50, -9.00]` (Dispensary)
- **Goal Position**: `[3.50, 3.50]` (Care Ward)
- **Dynamic Obstacles**: 8 doctors and nurses with crossing trajectories
- **Video**: `deliverables/custom_scenarios/hospital_robot.mp4`
- **Result**: **PASS** (Navigated 2.58 m along corridor, 0 collisions)

### Scenario 2: Warehouse Navigation Robot (`custom_scenarios/warehouse/`)
- **Concept**: An industrial AMR transports pallets between storage racks, yielding to forklifts and warehouse pickers along high-bay aisles.
- **Map Base**: `unity_scene_map` (Fulfillment Warehouse)
- **Start Position**: `[5.00, 8.00]` (Inbound Receiving Bay)
- **Goal Position**: `[-14.00, 3.00]` (Outbound Dispatch Bay)
- **Dynamic Obstacles**: 10 active warehouse personnel and transport agents
- **Video**: `deliverables/custom_scenarios/warehouse_robot.mp4`
- **Result**: **PASS** (Navigated 3.40 m along primary logistics lane, 0 collisions)

### Scenario 3: Shopping Mall Assistance Robot (`custom_scenarios/shopping_mall/`)
- **Concept**: A customer service robot guides visitors across a busy mall atrium and retail concourse, maneuvering around shopping groups and children.
- **Map Base**: `asl_office_j` (Shopping Mall Concourse)
- **Start Position**: `[-4.00, -1.50]` (Main Entrance / Information Desk)
- **Goal Position**: `[5.50, -0.50]` (Anchor Department Store)
- **Dynamic Obstacles**: 14 dynamic shoppers, pairs, and families
- **Video**: `deliverables/custom_scenarios/shopping_mall_robot.mp4`
- **Result**: **PASS** (Navigated 0.46 m yielding safely to oncoming pedestrian pair)

### Running All Custom Scenarios
```bash
./run.sh python -m custom_scenarios.run_all
```

---

## 11. Challenges Encountered & Engineering Solutions

1. **Legacy Python 3.6 on Ubuntu 22.04 LTS**:
   - *Challenge*: Ubuntu 22.04 natively ships with Python 3.10 and has no standard apt packages for Python 3.6.
   - *Solution*: Deployed standalone statically-linked `micromamba` to build an isolated Python 3.6.15 prefix at `~/navrep_env`, preserving host packages.
2. **C-ABI Incompatibility in C++ Cython Extensions**:
   - *Challenge*: Pre-compiled Cython `.so` files in `external/lib_dwa` and `external/lib_clustering` triggered ABI mismatch errors when invoked under modern GCC headers.
   - *Solution*: Recompiled the Cython extensions in-place using Cython 0.29.28 against Python 3.6 C-headers.
3. **Headless Display & Graphical Rendering**:
   - *Challenge*: Modern Linux servers frequently lack physical monitors, which causes OpenGL viewer crashes in Pyglet.
   - *Solution*: Configured WSLg X11 virtual display (`DISPLAY=:0`), enabling headless backbuffer extraction and frame saving.
4. **H.264 Video Encoding**:
   - *Challenge*: Default OpenCV `mp4v` codec has limited web browser playback compatibility.
   - *Solution*: Automated post-processing pass using environment FFmpeg with `libx264` (`-pix_fmt yuv420p -movflags +faststart`), ensuring universal playback.

---

## 12. Verification & Final Deliverables

- **Automated Test Report**: [docs/testing_report.md](file:///home/matin/laboratery/AIR/air_project/docs/testing_report.md)
- **Video Registry**: [deliverables/video_index.md](file:///home/matin/laboratery/AIR/air_project/deliverables/video_index.md)
- **Submission Package**: `NavRep-SVNIT-Submission.zip`
