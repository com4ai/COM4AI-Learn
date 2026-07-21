#!/usr/bin/env bash
set -euo pipefail

if ! command -v python3.12 >/dev/null 2>&1; then
    echo "Python 3.12 is required for this example."
    echo "On macOS with Homebrew, run: brew install python@3.12"
    exit 1
fi

python3.12 -m venv .venv-open-weight
source .venv-open-weight/bin/activate

python -m pip install --upgrade pip
python -m pip install torch "transformers>=4.37,<5" "numpy<2"

echo "Setup complete."
echo "Run the local model with: python open_weight_app.py"
