# Simulation Video Index and Deliverables Registry

**Project**: NavRep – Autonomous Robot Navigation and Simulation  
**Course**: CS359 – Artificial Intelligence for Robotics  
**Institution**: SVNIT Surat  

---

## 1. Technical Video Recording Specifications

All simulation videos in this registry were rendered directly from the running simulation environment and encoded to industry-standard high-efficiency H.264:

- **Format**: MP4 (`.mp4`) Container
- **Video Codec**: H.264 / AVC (Advanced Video Coding, High Profile)
- **Pixel Format**: YUV420p (broadest hardware & browser playback compatibility)
- **Framerate**: 20.0 FPS
- **Frame Resolution**: 512 x 512 pixels
- **Audio**: None (Silent Robotics Simulation)
- **Recording Engine**: Direct Pyglet OpenGL Backbuffer capture with OpenCV and FFmpeg post-processing

---

## 2. Custom Scenarios Video Registry

| File Name | Scenario Name | Map | Start $(x,y)$ | Goal $(x,y)$ | Pedestrians | Video Size | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `hospital_robot.mp4` | Hospital Assistance Robot | `asl` | `[-8.5, -9.0]` | `[3.5, 3.5]` | 8 | ~255 KB | Hospital corridor supply delivery; yields to doctors and crossing nurses. |
| `warehouse_robot.mp4` | Warehouse Navigation Robot | `unity_scene_map` | `[5.0, 8.0]` | `[-14.0, 3.0]` | 10 | ~257 KB | AMR logistics traversal between storage racks and pickers to outbound dock. |
| `shopping_mall_robot.mp4` | Shopping Mall Assistance | `asl_office_j` | `[-4.0, -1.5]` | `[5.5, -0.5]` | 14 | ~349 KB | Customer escort through crowded mall concourse avoiding crossing shoppers. |

---

## 3. Existing Scenarios Video Registry (All 27 Benchmark Scenarios)

| # | Standard File | Descriptive File | Map | Start $(x,y)$ | Goal $(x,y)$ | Pedestrians | Status | Description |
| :- | :--- | :--- | :--- | :--- | :--- | :-: | :-: | :--- |
| **01** | `scenario_01.mp4` | `scenario_01_irosasl1.mp4` | `asl` | `[1.3, -2.62]` | `[-6.65, -2.64]` | 26 | **PASS** | Dense crowd corridor navigation with active obstacle avoidance. |
| **02** | `scenario_02.mp4` | `scenario_02_irosasl2.mp4` | `asl` | `[-10.36, -10.03]` | `[5.12, 5.02]` | 0 | **PASS** | Long-distance static wall and corridor traversal across ASL floor. |
| **03** | `scenario_03.mp4` | `scenario_03_irosasl3.mp4` | `asl` | `[-9.3, -11.24]` | `[5.17, 5.24]` | 19 | **PASS** | Diagonal cross-lab traversal through multi-pedestrian clusters. |
| **04** | `scenario_04.mp4` | `scenario_04_irosasl4.mp4` | `asl` | `[4.96, -6.51]` | `[5.04, 1.6]` | 8 | **PASS** | Vertical corridor tracking with intersecting human agents. |
| **05** | `scenario_05.mp4` | `scenario_05_irosasl5.mp4` | `asl` | `[-6.31, -11.43]` | `[-6.43, 6.29]` | 9 | **PASS** | Full-length north-south hallway navigation past side offices. |
| **06** | `scenario_06.mp4` | `scenario_06_irosasl6.mp4` | `asl` | `[-9.3, -11.24]` | `[5.17, 5.24]` | 9 | **PASS** | High-velocity traversal with sparse dynamic obstacle avoidance. |
| **07** | `scenario_07.mp4` | `scenario_07_irosasl_office_j1.mp4` | `asl_office_j` | `[-21.41, -4.02]` | `[-24.37, 3.23]` | 15 | **PASS** | Tight office junction negotiation with multiple office workers. |
| **08** | `scenario_08.mp4` | `scenario_08_irosasl_office_j2.mp4` | `asl_office_j` | `[-21.53, -3.5]` | `[13.51, 7.39]` | 0 | **PASS** | Extensive static office corridor navigation from west wing to east. |
| **09** | `scenario_09.mp4` | `scenario_09_irosasl_office_j3.mp4` | `asl_office_j` | `[5.06, -1.09]` | `[-2.87, 6.11]` | 10 | **PASS** | Central concourse diagonal navigation with dynamic pedestrians. |
| **10** | `scenario_10.mp4` | `scenario_10_irosasl_office_j4.mp4` | `asl_office_j` | `[-3.55, -1.53]` | `[5.42, -0.57]` | 8 | **PASS** | Main hallway transit with counter-flow pedestrian avoidance. |
| **11** | `scenario_11.mp4` | `scenario_11_irosasl_office_j5.mp4` | `asl_office_j` | `[-22.69, -3.98]` | `[1.18, -1.05]` | 7 | **PASS** | West corridor approach to central atrium with dynamic crossing. |
| **12** | `scenario_12.mp4` | `scenario_12_irosasl_office_j6.mp4` | `asl_office_j` | `[-21.65, -3.33]` | `[13.81, 7.07]` | 6 | **PASS** | End-to-end office facility traversal past moving personnel. |
| **13** | `scenario_13.mp4` | `scenario_13_irosunity_scene_map1.mp4` | `unity_scene_map` | `[5.16, 9.35]` | `[-4.12, 9.57]` | 17 | **PASS** | High-density warehouse aisle cross-transit with pickers. |
| **14** | `scenario_14.mp4` | `scenario_14_irosunity_scene_map2.mp4` | `unity_scene_map` | `[1.03, -8.8]` | `[-17.44, 5.5]` | 0 | **PASS** | Static industrial warehouse perimeter obstacle avoidance. |
| **15** | `scenario_15.mp4` | `scenario_15_irosunity_scene_map3.mp4` | `unity_scene_map` | `[3.67, 8.65]` | `[5.64, -8.55]` | 17 | **PASS** | Vertical aisle descent through crowded storage lanes. |
| **16** | `scenario_16.mp4` | `scenario_16_irosunity_scene_map4.mp4` | `unity_scene_map` | `[-0.07, 0.27]` | `[-16.96, 0.4]` | 8 | **PASS** | Central warehouse cross-dock transit with dynamic traffic. |
| **17** | `scenario_17.mp4` | `scenario_17_irosunity_scene_map5.mp4` | `unity_scene_map` | `[-3.69, -8.23]` | `[-3.53, 9.11]` | 7 | **PASS** | Full-height warehouse storage bay navigation. |
| **18** | `scenario_18.mp4` | `scenario_18_irosunity_scene_map6.mp4` | `unity_scene_map` | `[5.01, -0.26]` | `[-17.99, -0.23]` | 14 | **PASS** | Horizontal logistics corridor tracking across multiple aisles. |
| **19** | `scenario_19.mp4` | `scenario_19_rlasl1.mp4` | `asl` | `[-3.93, -4.14]` | `[-1.23, -1.29]` | 0 | **PASS** | Curriculum Level 1: Short-range direct navigation in open space. |
| **20** | `scenario_20.mp4` | `scenario_20_rlasl2.mp4` | `asl` | `[-8.39, -4.93]` | `[-7.11, -8.08]` | 0 | **PASS** | Curriculum Level 2: Static corridor turn navigation. |
| **21** | `scenario_21.mp4` | `scenario_21_rlasl3.mp4` | `asl` | `[-0.2, -1.88]` | `[-3.44, -3.35]` | 9 | **PASS** | Curriculum Level 3: Dynamic crowd navigation in ASL floor. |
| **22** | `scenario_22.mp4` | `scenario_22_rlasl_office_j1.mp4` | `asl_office_j` | `[-21.03, -3.95]` | `[-21.76, -1.34]` | 0 | **PASS** | Curriculum Level 1 (Office): Short static office corridor goal. |
| **23** | `scenario_23.mp4` | `scenario_23_rlasl_office_j2.mp4` | `asl_office_j` | `[-22.79, -0.26]` | `[-22.67, 3.38]` | 0 | **PASS** | Curriculum Level 2 (Office): Medium office hallway transit. |
| **24** | `scenario_24.mp4` | `scenario_24_rlasl_office_j3.mp4` | `asl_office_j` | `[-21.05, -4.3]` | `[-21.22, -2.08]` | 7 | **PASS** | Curriculum Level 3 (Office): Office junction crowd avoidance. |
| **25** | `scenario_25.mp4` | `scenario_25_rlunity_scene_map1.mp4` | `unity_scene_map` | `[2.88, 0.41]` | `[-0.91, 0.3]` | 0 | **PASS** | Curriculum Level 1 (Unity): Short open aisle navigation. |
| **26** | `scenario_26.mp4` | `scenario_26_rlunity_scene_map2.mp4` | `unity_scene_map` | `[0.62, 1.39]` | `[1.11, 5.25]` | 0 | **PASS** | Curriculum Level 2 (Unity): Mid-range aisle traversal. |
| **27** | `scenario_27.mp4` | `scenario_27_rlunity_scene_map3.mp4` | `unity_scene_map` | `[4.51, 1.9]` | `[1.44, -0.63]` | 9 | **PASS** | Curriculum Level 3 (Unity): Dynamic warehouse picker avoidance. |

---

## 4. Verification & Playback

Every video file is directly accessible in:
- `deliverables/existing_scenarios/`
- `deliverables/custom_scenarios/`

Videos can be played using any media player (`vlc`, `mpv`, Windows Media Player, QuickTime) or embedded directly in Markdown and web browsers.
