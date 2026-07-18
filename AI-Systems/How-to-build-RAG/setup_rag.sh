#!/usr/bin/env bash

set -euo pipefail

if ! command -v python3.12 >/dev/null 2>&1; then
    echo "Python 3.12 is required. On macOS, install it with: brew install python@3.12"
    exit 1
fi

python3.12 -m venv .venv-rag
source .venv-rag/bin/activate

python -m pip install --upgrade pip
python -m pip install "numpy<2" torch "transformers>=4.37,<5" sentence-transformers

echo
echo "Setup complete. Start the RAG application with:"
echo "source .venv-rag/bin/activate"
echo "python rag_app.py"

