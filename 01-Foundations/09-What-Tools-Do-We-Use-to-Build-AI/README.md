# What Tools Do We Use to Build AI?

Building AI is not only about choosing a model. You also need tools to write code, manage dependencies, explore data, train or call models, track changes, test results, and run the finished application.

You do not need every tool on day one. Start with a small, reliable setup and add tools as your projects become more complex.

```text
Idea → code and data → model → evaluation → application → deployment and monitoring
```

## The AI Builder’s Toolbox

| Tool category | Why it matters | Beginner examples |
|---|---|---|
| **Programming language** | Defines the application and data-processing logic. | Python, JavaScript/TypeScript. |
| **Data tools** | Read, clean, transform, and visualize data. | pandas, NumPy, SQL, matplotlib. |
| **ML framework** | Builds, trains, or evaluates machine-learning models. | scikit-learn, PyTorch, TensorFlow. |
| **Model access** | Uses hosted APIs or downloads open-weight models. | OpenAI API, Hugging Face, Ollama. |
| **Deployment tools** | Makes an AI application available to users. | FastAPI, Docker, cloud platforms. |
| **Monitoring and evaluation** | Checks quality, cost, latency, and failures after release. | Logs, tests, dashboards, evaluation datasets. |

## A Practical Beginner Setup

For the Foundations lessons, focus on the tools closest to the AI workflow:

```text
Python + data tools + ML framework or model API + evaluation + deployment tools
```

This is enough to prepare data, use a model, test its outputs, and turn it into an application.

### Example: A Small AI Project

```text
my-ai-project/
├── data/               # project data
├── app.py              # application code
├── model/              # trained model or model configuration
├── tests/              # evaluation examples and automated tests
├── README.md           # instructions and explanation
└── deploy/             # deployment configuration, when needed
```

The exact folders change from project to project, but this structure keeps data, model use, evaluation, and application code separate.

## 1. Programming Languages

Programming languages tell the computer how to prepare data, call a model, process a response, and build an application interface.

### Python

Python is a common starting point for AI because it has a large ecosystem for data science, machine learning, automation, and web applications.

```text
Python code → data or model library → result
```

Common Python libraries include:

| Library | Typical use |
|---|---|
| **NumPy** | Arrays and numerical calculations. |
| **pandas** | Tables, CSV files, and data cleaning. |
| **matplotlib** | Charts and visualizations. |
| **scikit-learn** | Classical machine-learning models and evaluation. |
| **PyTorch** | Neural networks and deep learning. |
| **Transformers** | Using many pretrained language, image, and audio models. |

## 2. Data Tools

AI systems depend on data. Data tools help you inspect, clean, transform, store, and visualize it.

### Example: Customer-Order Data

```text
CSV file → pandas table → clean missing values → calculate features → model input
```

| Tool | Typical job |
|---|---|
| **CSV/JSON files** | Store small, simple datasets. |
| **pandas** | Read tables, filter rows, clean columns, and summarize data. |
| **NumPy** | Work efficiently with numerical arrays. |
| **SQL** | Query data stored in relational databases. |
| **matplotlib or seaborn** | Visualize distributions, trends, and errors. |

Use the smallest data tool that fits the problem. A CSV file is enough for many learning projects; larger applications may need a database, data pipeline, and access controls.

## 3. Machine-Learning and Deep-Learning Frameworks

Frameworks provide reusable implementations of model algorithms and training tools.

| Framework | Best starting use |
|---|---|
| **scikit-learn** | Regression, classification, clustering, preprocessing, and evaluation for structured data. |
| **PyTorch** | Building and training neural networks; research and production work. |
| **TensorFlow/Keras** | Building and training neural networks with a high-level API. |
| **Transformers** | Loading and using many pretrained transformer models. |

### Example: Choose a Framework

```text
Predict house prices from spreadsheet columns → scikit-learn
Train an image-recognition neural network → PyTorch or TensorFlow
Run a pretrained language model → Transformers or a model-serving tool
```

Do not choose a complex framework merely because it is popular. Start with the simplest tool that can solve the problem and evaluate whether it works.

## 4. Models: Hosted APIs and Open-Weight Models

There are two main ways to use a modern AI model:

```text
Hosted model:       application → provider API → model response
Open-weight model:  application → local/server inference → model response
```

| Approach | Common tools | What you manage |
|---|---|---|
| **Hosted API** | Provider SDKs and HTTP APIs. | Your application, prompts, security, costs, and integration. |
| **Open-weight model** | Hugging Face, Ollama, llama.cpp, vLLM, Transformers. | Model files, hardware, inference, updates, and deployment. |

### Example: First Chat Application

```text
Hosted API route:
Python application → model API → generated reply

Open-weight route:
Python application → local model runtime → generated reply
```

A hosted API is often the simplest first step. An open-weight model can provide more control, local execution, or privacy, but it requires suitable hardware and more operational work.

## 5. Testing and Evaluation Tools

Every AI project needs a repeatable way to check that it still works after a change.

### Example: Test Cases for a Support Assistant

```text
Test 1: A normal product question → answer is accurate
Test 2: An unclear request → assistant asks a clarifying question
Test 3: A request for private account data → assistant refuses or escalates safely
Test 4: A provider outage → application shows a helpful error
```

Tools can include automated tests, an evaluation dataset, logs, manual review, and dashboards. The right choice depends on the AI task and its risks.

## 6. Deployment and Operations Tools

After a local program works, deployment tools package it and make it available to users.

```text
Local code → web API or user interface → deployment platform → users
```

| Tool or concept | Purpose |
|---|---|
| **FastAPI or Flask** | Build a Python web API around an AI application. |
| **Docker** | Package an application and its dependencies consistently. |
| **Cloud platform** | Run the application, store data, and scale resources. |
| **Environment variables** | Supply configuration and secrets without putting them in source code. |
| **Logging and monitoring** | Track errors, usage, latency, cost, and quality. |

### Example: Keep an API Key Out of Code

```text
Wrong:  api_key = "secret-key" inside app.py
Right:  API key stored in an environment variable or secret manager
```

This protects secrets from accidental sharing in Git or screenshots.

## An End-to-End Beginner Workflow

Imagine building a simple application that classifies support messages:

```text
1. Define the categories: billing, technical issue, general question
2. Use pandas to inspect example messages and labels
3. Prepare data and create useful features
4. Build a first model with scikit-learn or call a hosted model API
5. Evaluate it on held-out examples and inspect mistakes
6. Add safety and error-handling tests
7. Package the application as an API when it is ready for users
8. Monitor errors, cost, latency, and output quality
9. Improve the data, model, or prompts over time
```

The tools support the workflow; they are not the goal. Choose tools that keep your project understandable, reproducible, and safe.

## Recommended Learning Order

1. Learn basic Python and how to work with data.
2. Explore data with pandas, NumPy, and simple charts.
3. Use scikit-learn for first structured-data models.
4. Learn PyTorch or TensorFlow when you need neural networks.
5. Use a hosted API or small open-weight model for AI applications.
6. Evaluate results with test data, metrics, and error analysis.
7. Add deployment, monitoring, and safety checks as projects grow.

## Key Takeaways

- AI development uses a toolkit, not one single program or model.
- Data tools, ML frameworks, and model runtimes should match the problem you are solving.
- Hosted APIs simplify model access; open-weight models provide greater control but require more infrastructure.
- Keep secrets and local environment folders out of Git.
- Testing, evaluation, deployment, and monitoring are part of building a dependable AI application.

## References

- [scikit-learn: Getting Started](https://scikit-learn.org/stable/getting_started.html) — official introduction to data preprocessing, model fitting, evaluation, and pipelines.
- [PyTorch Tutorials](https://docs.pytorch.org/tutorials/) — official learning resources for neural networks and deep learning.
- [Hugging Face documentation](https://huggingface.co/docs) — documentation for open models, datasets, and machine-learning libraries.
- [FastAPI documentation](https://fastapi.tiangolo.com/) — official guide to building Python web APIs.
