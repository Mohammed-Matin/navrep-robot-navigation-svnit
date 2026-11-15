#!/usr/bin/env bash
# ==============================================================================
# NavRep-SVNIT Setup Script
# Reproducible environment installer for SVNIT CS359 AI for Robotics Project
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_DIR="${HOME}/navrep_env"
MAMBA_BIN="${HOME}/.local/bin/micromamba"

echo "=== [1/6] Checking Micromamba Package Manager ==="
mkdir -p "${HOME}/.local/bin"
if [ ! -x "${MAMBA_BIN}" ]; then
    echo "Downloading standalone micromamba binary..."
    curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj -C "${HOME}/.local/bin/" --strip-components=1 bin/micromamba
fi
"${MAMBA_BIN}" --version

echo "=== [2/6] Setting Up Isolated Python 3.6 Environment ==="
if [ ! -d "${ENV_DIR}" ]; then
    "${MAMBA_BIN}" create -y -p "${ENV_DIR}" -c conda-forge python=3.6.15 pip ffmpeg
else
    echo "Environment already exists at ${ENV_DIR}"
fi

PYTHON_EXEC="${ENV_DIR}/bin/python"
PIP_EXEC="${ENV_DIR}/bin/pip"

echo "=== [3/6] Installing Core Scientific & Robotics Dependencies ==="
export PYTHONPATH=""

# 1. Base build dependencies
"${PIP_EXEC}" install "numpy==1.19.5" "Cython==0.29.28"

# 2. Scientific & plotting
"${PIP_EXEC}" install \
    "matplotlib==3.3.4" "pandas==1.1.0" "scipy==1.5.4" \
    "pyyaml==6.0" "rospkg==1.4.0" "catkin_pkg==0.4.24" \
    "numba==0.53.1" "tqdm==4.63.0" "rich==12.0.0"

# 3. Deep Learning & RL framework
"${PIP_EXEC}" install "tensorflow==1.13.2" "keras==2.3.1"
"${PIP_EXEC}" install "opencv-python==4.5.5.64"
"${PIP_EXEC}" install "cloudpickle==1.6.0" "pyglet==1.5.22" "joblib==1.1.0" "gym==0.15.7"
"${PIP_EXEC}" install --no-deps "stable-baselines==2.10.0"
"${PIP_EXEC}" install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

echo "=== [4/6] Installing NavRep Domain & Simulator Packages ==="
"${PIP_EXEC}" install \
    "asl-pepper-2d-sim==0.0.5" \
    "soadrl-crowdnav==0.0.3" \
    "pyIAN==0.0.3" \
    "pyniel==0.2" \
    "pymap2d==0.1.15" \
    "pylidar2d==0.1" \
    "pyrvo2-danieldugas==0.0.2"

# Compile RangeLibc using in-env Cython without build isolation
"${PIP_EXEC}" install --no-build-isolation "pyrangelibc-danieldugas==0.0.2"

# Pure-python ROS packages from rospypi
"${PIP_EXEC}" install --extra-index-url https://rospypi.github.io/simple/ \
    rospy rosbag tf tf2_ros genpy geometry-msgs sensor-msgs std-msgs nav-msgs tf2-msgs actionlib-msgs tf2-py

echo "=== [5/6] Building Local Extensions and Packages ==="
"${PIP_EXEC}" install -e "${SCRIPT_DIR}/external/lib_clustering"
"${PIP_EXEC}" install -e "${SCRIPT_DIR}/external/lib_dwa"
cp -rn "${SCRIPT_DIR}/external/frame_msgs" "${ENV_DIR}/lib/python3.6/site-packages/" || true
cp -rn "${SCRIPT_DIR}/external/tf_bag" "${ENV_DIR}/lib/python3.6/site-packages/" || true

# Install NavRep editable
cd "${SCRIPT_DIR}"
"${PIP_EXEC}" install -e . --no-deps

echo "=== [6/6] Verifying Installation ==="
PYTHONPATH="" "${PYTHON_EXEC}" -c "
import navrep, navrep.envs, navrep.models, crings, gym, tensorflow as tf, torch
from stable_baselines import PPO2
print('========================================')
print('NavRep verification PASSED!')
print('Python:', sys.version.split()[0] if 'sys' in locals() else '3.6.15')
print('TensorFlow:', tf.__version__)
print('PyTorch:', torch.__version__)
print('Gym:', gym.__version__)
print('========================================')
"

echo "Setup completed successfully! Use ./run.sh to execute scripts."
