# 03: Building Your First LLM Application

Build a simple application that sends a request to an LLM and displays its response.

## Files

- `setup.sh` creates a Python virtual environment and installs the OpenAI SDK.
- `app.py` asks for a question, sends it to a hosted LLM, and prints the response.

## How to Run

From this folder, run the setup once:

```bash
chmod +x setup.sh
./setup.sh
```

Before running the application, create an API key in the OpenAI Platform and set it in your terminal. Never add the key to `app.py` or commit it to GitHub.

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Then activate the environment and run the program:

```bash
source .venv/bin/activate
python app.py
```
