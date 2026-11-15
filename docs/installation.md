# Installation and Environment Configuration Guide

**Project**: NavRep – Robot Navigation and Simulation  
**Course**: CS359 – Artificial Intelligence for Robotics  
**Institution**: Sardar Vallabhbhai National Institute of Technology (SVNIT), Surat  
**Department**: Department of Computer Science and Engineering  

---

## 1. System Specifications & Compatibility Matrix

| Specification | Host Development Environment |
| :--- | :--- |
| **Operating System** | Ubuntu 22.04.5 LTS (Linux kernel 6.6.87.2-microsoft-standard-WSL2) |
| **Architecture** | x86_64 (64-bit Intel Core i5-11400H @ 2.70 GHz) |
| **System Memory** | 3.7 GiB Available Virtual RAM + 8 GiB Swap |
| **Target Python** | Python 3.6.15 (Conda-Forge isolated environment) |
| **C/C++ Toolchain** | GCC 11.4.0 (Ubuntu) & Clang-compatible compiler |
| **Rendering Subsystem** | WSLg Wayland/X11 Virtual Server (`DISPLAY=:0`) + Pyglet OpenGL |
| **Video Encoding** | FFmpeg 7.0.2 with `libx264` (H.264 High Profile, YUV420p) |

---

## 2. Technical Architecture & Isolation Design

NavRep originally depends on legacy robotics and reinforcement learning software packages:
- **Python 3.6** (deprecated in modern Ubuntu 22.04 LTS package repositories)
- **OpenAI Gym 0.15.7**
- **TensorFlow 1.13.2** & **Keras 2.3.1**
- **Stable-Baselines 2.10.0**
- **PyTorch 1.6.0 CPU**
- **ROS 1 Melodic/Noetic** Python communication bindings

To preserve system package integrity and prevent host contamination, all dependencies are installed into an isolated environment at `~/navrep_env` using standalone `micromamba`.

---

## 3. Automated Quick Installation

A fully automated, idempotent setup script is provided:

```bash
chmod +x setup.sh run.sh
./setup.sh
```

The script runs the complete 6-stage setup pipeline:
1. **Micromamba Bootstrap**: Downloads the standalone statically-linked micromamba executable to `~/.local/bin/micromamba`.
2. **Environment Creation**: Builds an isolated prefix at `~/navrep_env` with `python=3.6.15`, `pip`, and `ffmpeg`.
3. **Core Dependencies**: Builds and pins `numpy==1.19.5` and `Cython==0.29.28`.
4. **Deep Learning Frameworks**: Installs `tensorflow==1.13.2`, `keras==2.3.1`, `torch==1.6.0+cpu`, `gym==0.15.7`, and `stable-baselines==2.10.0`.
5. **Robotics Domain Packages**: Installs `asl-pepper-2d-sim`, `pyIAN`, `pyrangelibc`, `pyrvo2`, `pymap2d`, `pylidar2d`, and pure-Python ROS 1 message packages from `rospypi`.
6. **Local Extension Build**: Compiles local C++/Cython extensions (`crings`, `lib_clustering`, `lib_dwa`) and installs `navrep` in editable mode.

---

## 4. Manual Step-by-Step Installation

If you prefer to perform the installation step-by-step:

### Step 4.1: Download Micromamba
```bash
mkdir -p ~/.local/bin
curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj -C ~/.local/bin/ --strip-components=1 bin/micromamba
~/.local/bin/micromamba --version
```

### Step 4.2: Create Python 3.6 Prefix
```bash
~/.local/bin/micromamba create -y -p ~/navrep_env -c conda-forge python=3.6.15 pip ffmpeg
```

### Step 4.3: Install Pinned Dependencies
```bash
export ENV_DIR="${HOME}/navrep_env"
export PYTHON_EXEC="${ENV_DIR}/bin/python"
export PIP_EXEC="${ENV_DIR}/bin/pip"
export PYTHONPATH=""

# Build tools
"${PIP_EXEC}" install "numpy==1.19.5" "Cython==0.29.28"

# Scientific, formatting and robotics dependencies
"${PIP_EXEC}" install \
    "matplotlib==3.3.4" "pandas==1.1.0" "scipy==1.5.4" \
    "pyyaml==6.0" "rospkg==1.4.0" "catkin_pkg==0.4.24" \
    "numba==0.53.1" "tqdm==4.63.0" "rich==12.0.0"

# Deep learning & RL
"${PIP_EXEC}" install "tensorflow==1.13.2" "keras==2.3.1"
"${PIP_EXEC}" install "opencv-python==4.5.5.64"
"${PIP_EXEC}" install "cloudpickle==1.6.0" "pyglet==1.5.22" "joblib==1.1.0" "gym==0.15.7"
"${PIP_EXEC}" install --no-deps "stable-baselines==2.10.0"
"${PIP_EXEC}" install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

# NavRep domain simulators
"${PIP_EXEC}" install \
    "asl-pepper-2d-sim==0.0.5" \
    "soadrl-crowdnav==0.0.3" \
    "pyIAN==0.0.3" \
    "pyniel==0.2" \
    "pymap2d==0.1.15" \
    "pylidar2d==0.1" \
    "pyrvo2-danieldugas==0.0.2"

# Compile pyrangelibc without build isolation
"${PIP_EXEC}" install --no-build-isolation "pyrangelibc-danieldugas==0.0.2"

# Pure-python ROS packages
"${PIP_EXEC}" install --extra-index-url https://rospypi.github.io/simple/ \
    rospy rosbag tf tf2_ros genpy geometry-msgs sensor-msgs std-msgs nav-msgs tf2-msgs actionlib-msgs tf2-py
```

### Step 4.4: Compile Local Extensions and Install NavRep
```bash
# Compile local C++ extensions
"${PIP_EXEC}" install -e external/lib_clustering
"${PIP_EXEC}" install -e external/lib_dwa

# Install ROS helper message definitions
cp -rn external/frame_msgs "${ENV_DIR}/lib/python3.6/site-packages/" || true
cp -rn external/tf_bag "${ENV_DIR}/lib/python3.6/site-packages/" || true

# Install NavRep in editable mode
"${PIP_EXEC}" install -e . --no-deps
```

---

## 5. Execution Wrapper (`./run.sh`)

To avoid manual path exports and ensure clean environment activation, execute any script through the `./run.sh` wrapper:

```bash
# Test imports and environment health
./run.sh python -c "import navrep, gym, tensorflow; print('Environment operational!')"

# Execute all existing simulation scenarios and generate recordings
./run.sh python scripts/record_existing_scenarios.py

# Execute all custom simulation scenarios
./run.sh python -m custom_scenarios.run_all

# Run individual custom scenario
./run.sh python -m custom_scenarios.hospital.hospital_scenario
./run.sh python -m custom_scenarios.warehouse.warehouse_scenario
./run.sh python -m custom_scenarios.shopping_mall.shopping_mall_scenario
```

---

## 6. Verification Checklist

| Test Item | Verification Command | Expected Output | Status |
| :--- | :--- | :--- | :--- |
| **Python Version** | `./run.sh python --version` | `Python 3.6.15` | **PASS** |
| **TensorFlow & Keras** | `./run.sh python -c "import tensorflow, keras; print(tensorflow.__version__)"` | `1.13.2` | **PASS** |
| **Gym & Stable-Baselines** | `./run.sh python -c "import gym, stable_baselines; print(gym.__version__)"` | `0.15.7` | **PASS** |
| **NavRep Core** | `./run.sh python -c "import navrep, navrep.envs, crings; print('OK')"` | `OK` | **PASS** |
| **DWA C++ Extension** | `./run.sh python -c "import dynamic_window; print(dir(dynamic_window))"` | Linear DWA & Planner list | **PASS** |
| **Rendering Subsystem** | `./run.sh python -c "import pyglet; w=pyglet.window.Window(visible=False); w.close(); print('Pyglet OK')"` | `Pyglet OK` | **PASS** |
