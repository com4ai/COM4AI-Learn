#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install openai

echo "Setup complete."
echo "Set your key with: export OPENAI_API_KEY=\"your_api_key_here\""
echo "Then run: python hosted_llm_app.py"
