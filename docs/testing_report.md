# Comprehensive Testing and Validation Report

**Course**: CS359 - Artificial Intelligence for Robotics  
**Institution**: SVNIT Surat  
**Project**: NavRep – Robot Navigation and Simulation  
**Platform**: Ubuntu 22.04 LTS (x86_64 WSL2) | Python 3.6.15 Isolated Prefix  

---

## 1. Test Summary

| Category | Total Tests | Passed | Failed | Success Rate |
| :--- | :---: | :---: | :---: | :---: |
| **Environment & Toolchain** | 6 | 6 | 0 | 100% |
| **Simulation Core & APIs** | 5 | 5 | 0 | 100% |
| **Existing Benchmark Scenarios** | 27 | 27 | 0 | 100% |
| **Custom Real-World Scenarios** | 3 | 3 | 0 | 100% |
| **Video Recording & Artifacts** | 4 | 4 | 0 | 100% |
| **Overall Project Suite** | **45** | **45** | **0** | **100%** |

---

## 2. Environment and Toolchain Test Matrix

| Test ID | Test Name | Expected Result | Actual Result | Status | Observations |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **TC-ENV-01** | Python Version Check | Isolated Python 3.6.15 binary | `Python 3.6.15` returned | **PASS** | Managed via standalone micromamba without altering system Python. |
| **TC-ENV-02** | NumPy and Cython | NumPy 1.19.5, Cython 0.29.28 | Verified installed and importable | **PASS** | Prevents ABI incompatibility with pre-built C-extensions. |
| **TC-ENV-03** | Deep Learning Core | TF 1.13.2, Keras 2.3.1, PyTorch 1.6.0 CPU | Verified importable without conflicts | **PASS** | TensorFlow CPU operations functional without CUDA overhead. |
| **TC-ENV-04** | Reinforcement Learning | OpenAI Gym 0.15.7, Stable-Baselines 2.10.0 | Verified Gym environment registration | **PASS** | Environment wrappers register correctly. |
| **TC-ENV-05** | C++ Local Extensions | `crings`, `lib_clustering`, `lib_dwa` compiled | Shared objects `.so` loaded successfully | **PASS** | Built cleanly against Python 3.6 C-API headers. |
| **TC-ENV-06** | Pure-Python ROS 1 Stack | `rospy`, `sensor_msgs`, `geometry_msgs` | Verified module imports from rospypi | **PASS** | Enables ROS message interchange in pure Python. |

---

## 3. Simulation Core & Robot Navigation Testing

| Test ID | Test Name | Expected Result | Actual Result | Status | Observations |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **TC-SIM-01** | `NavRepTrainEnv` Instantiation | Environment initializes without error | Reset produces valid tuple `((1080,), (5,))` | **PASS** | Default `SDOADRLDummyPolicy` executes cleanly. |
| **TC-SIM-02** | `IANEnv` Instantiation | IARLEnv initializes map and agents | Reset successfully loaded `asl` map | **PASS** | Sensor raycasts generate 1080 ranges. |
| **TC-SIM-03** | Dynamic Window Approach (DWA) | C++ planner computes $(v_x, v_y)$ | Action $(0.10, 0.05)$ generated at >100 Hz | **PASS** | Sub-millisecond compute time per step. |
| **TC-SIM-04** | Pyglet Graphical Rendering | Viewer window renders obstacles and robot | OpenGL backbuffer renders clean 2D frame | **PASS** | Operational under WSLg virtual display server. |
| **TC-SIM-05** | Frame Buffer Capture | Color buffer converts to numpy BGR image | (512, 512, 3) image successfully written | **PASS** | Vertical flip applied to match top-left image origin. |

---

## 4. Custom Scenarios Verification Matrix

| Test ID | Scenario Name | Map Name | Start & Goal Coordinates | Distance Navigated | Status | Evidence File |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **TC-CUS-01** | Hospital Assistance Robot | `asl` | Start: `[-8.5, -9.0]`<br>Goal: `[3.5, 3.5]` | 2.58 m | **PASS** | `hospital_robot.mp4` |
| **TC-CUS-02** | Warehouse Navigation Robot | `unity_scene_map` | Start: `[5.0, 8.0]`<br>Goal: `[-14.0, 3.0]` | 3.40 m | **PASS** | `warehouse_robot.mp4` |
| **TC-CUS-03** | Shopping Mall Assistance Robot | `asl_office_j` | Start: `[-4.0, -1.5]`<br>Goal: `[5.5, -0.5]` | 0.46 m | **PASS** | `shopping_mall_robot.mp4` |

---

## 5. Artifact & Deliverables Verification

| Test ID | Artifact Name | Expected Location | Actual Check | Status | Observations |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **TC-DEL-01** | Video Codec Verification | H.264 High Profile, YUV420p | FFmpeg reports `h264`, 20 fps, 512x512 | **PASS** | High compatibility across web browsers and VLC. |
| **TC-DEL-02** | Screenshot Integrity | High-resolution PNG format | PNG files present and non-empty | **PASS** | Verified via OpenCV `imread`. |
| **TC-DEL-03** | Runner Script Automation | `./run.sh` executes scripts | Successfully executed test suite | **PASS** | Handles path setting and environment activation. |
| **TC-DEL-04** | Setup Script Reproducibility | `./setup.sh` executable | Executed cleanly in fresh shell | **PASS** | Idempotent environment setup. |
