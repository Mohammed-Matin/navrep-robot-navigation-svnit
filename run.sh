#!/usr/bin/env bash
# ==============================================================================
# NavRep-SVNIT Runner Script
# Wrapper script to execute NavRep commands in the isolated environment
# ==============================================================================
set -euo pipefail

ENV_DIR="${HOME}/navrep_env"
PYTHON_EXEC="${ENV_DIR}/bin/python"

if [ ! -x "${PYTHON_EXEC}" ]; then
    echo "Error: Python environment not found at ${PYTHON_EXEC}."
    echo "Please run ./setup.sh first to set up the environment."
    exit 1
fi

export PYTHONPATH=""
export PATH="${ENV_DIR}/bin:${PATH}"

if [ "$#" -eq 0 ]; then
    echo "Usage: ./run.sh [python_script_or_command] [args...]"
    echo "Examples:"
    echo "  ./run.sh python -m navrep.scripts.test_navrep"
    echo "  ./run.sh python -m custom_scenarios.run_all"
    exit 0
fi

if [ "$1" = "python" ]; then
    shift
    exec "${PYTHON_EXEC}" "$@"
else
    exec "${PYTHON_EXEC}" "$@"
fi
