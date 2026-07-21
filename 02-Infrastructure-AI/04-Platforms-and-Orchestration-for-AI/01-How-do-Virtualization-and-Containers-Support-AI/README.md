# How Do Virtualization and Containers Support AI?

AI applications need a dependable environment in which to run. **Virtual machines** and **containers** make it possible to package, isolate, move, and reproduce that environment on a developer laptop, an on-premises server, or a cloud platform.

They solve related but different problems:

```text
Physical server
├── Virtual machines: isolate complete operating systems
└── Containers: package applications and share the host operating system
```

## What Is Virtualization?

**Virtualization** uses a layer called a **hypervisor** to divide one physical computer into multiple isolated virtual machines (VMs). Each VM has virtual CPU, memory, storage, network interfaces, and its own guest operating system.

```text
Physical server
        ↓
Hypervisor
├── VM 1: operating system + AI application
├── VM 2: operating system + database
└── VM 3: operating system + monitoring tools
```

For AI, VMs are useful when teams need strong isolation between projects, users, or customers. A cloud provider can give a team a VM with a selected CPU, GPU, memory size, storage volume, and network configuration without giving it access to the entire physical server.

## What Is a Container?

A **container** packages an application with its libraries, runtime, and configuration. Unlike a VM, a container does not include a full guest operating system. Multiple containers share the host operating system kernel while remaining isolated from one another.

```text
Host operating system
├── Container: AI API + Python libraries
├── Container: model-serving application
└── Container: database or vector store
```

For example, an AI service might need a particular Python version, PyTorch version, CUDA libraries, and model-serving package. A container image records that environment so it can run consistently on a developer computer, test server, or cloud cluster.

## Virtual Machines and Containers Compared

| Topic | Virtual machine | Container |
|---|---|---|
| **Isolation level** | Isolates a complete guest operating system. | Isolates an application process while sharing the host kernel. |
| **Size and startup time** | Usually larger and slower to start. | Usually smaller and faster to start. |
| **Operating system** | Each VM includes its own guest OS. | Containers share the host OS kernel. |
| **Typical AI use** | Isolated development, cloud instances, multi-tenant environments, and different operating-system needs. | Reproducible AI services, model serving, pipelines, and deployment. |
| **Common tools** | Hyper-V, VMware, KVM, and cloud virtual machines. | Docker, containerd, Podman, and Kubernetes. |

Containers do not replace virtual machines in every situation. Many cloud and data-center setups use both: a VM provides the server boundary, and containers run applications inside that VM.

```text
Cloud physical server
        ↓
Virtual machine
        ↓
Container runtime
        ↓
AI application container
```

## Why Containers Matter for AI

AI projects have many dependencies: Python packages, operating-system libraries, model runtimes, GPU drivers, and service configuration. Without a repeatable package, an application that works on one computer may fail on another.

Containers help teams:

- reproduce the same AI environment across development, testing, and production;
- package an AI API, model server, vector database, or data-processing job separately;
- deploy new versions more predictably; and
- run multiple services together without mixing their dependencies.

## A Simple AI Deployment Example

```text
User request
        ↓
Web or API container
        ↓
Model-serving container
        ↓
Model files, database, or vector store
        ↓
Response to the user
```

Each part can be packaged separately. Later, an orchestration platform such as Kubernetes can run several copies of these containers, restart failed copies, and distribute them across available machines.

## Example: Containerize a Small AI API

This example packages a small Python API in a Docker image. The API accepts text and returns a simple classification result. The classification function is deliberately small so the example focuses on **containerization**; in a real project, replace it with code that loads and calls your model.

Create a folder named `ai-api` with these files:

```text
ai-api/
├── app.py
├── requirements.txt
└── Dockerfile
```

### 1. Create the API

`app.py`:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PredictionRequest(BaseModel):
    text: str


@app.post("/predict")
def predict(request: PredictionRequest):
    text = request.text.lower()
    label = "positive" if "good" in text or "great" in text else "other"

    return {"text": request.text, "label": label}
```

`requirements.txt`:

```text
fastapi
uvicorn[standard]
```

### 2. Create the Dockerfile

A `Dockerfile` tells Docker how to build the application image.

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

What each instruction does:

| Dockerfile instruction | Purpose |
|---|---|
| `FROM` | Starts from an existing Python runtime image. |
| `WORKDIR` | Sets `/app` as the working folder inside the container. |
| `COPY` | Copies project files into the image. |
| `RUN` | Installs the Python dependencies while the image is being built. |
| `EXPOSE` | Documents that the API listens on port 8000. |
| `CMD` | Starts the API whenever a container starts. |

### 3. Build and Run the Container

From the `ai-api` folder, run:

```bash
docker build -t ai-api:1.0 .
docker run --rm -p 8000:8000 ai-api:1.0
```

The first command builds an image named `ai-api:1.0`. The second starts a container from that image and maps your computer's port 8000 to port 8000 inside the container.

In another terminal, send a request:

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"This is a great example"}'
```

Expected response:

```json
{"text":"This is a great example","label":"positive"}
```

The same image can be run by another developer, a test server, or Kubernetes, without separately installing Python, FastAPI, or Uvicorn on each environment.

### 4. Add a Real Model Later

For a real AI service, the application code can load a model at startup:

```python
# Example only: load your chosen model here when the container starts.
# model = load_model("/models/my-model")

@app.post("/predict")
def predict(request: PredictionRequest):
    # result = model.predict(request.text)
    return {"result": "replace this with the model output"}
```

For large models, keep in mind where model weights come from. You can include small fixed assets in the image, download a model during startup, or mount model storage into the container. The best choice depends on model size, update frequency, startup time, and deployment platform.

## Key Takeaways

- Virtualization creates isolated virtual computers on shared physical hardware.
- Containers package applications and dependencies while sharing the host operating system.
- VMs provide stronger operating-system isolation; containers are generally lighter and faster to deploy.
- AI systems often use VMs for infrastructure boundaries and containers for reproducible applications and services.
- Kubernetes commonly manages containers at scale, which is the next lesson in this section.

## References

- [Microsoft Learn: Hyper-V overview](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/overview) — official introduction to hypervisors and virtual machines.
- [Docker: Get started](https://docs.docker.com/get-started/) — official introduction to Docker and containerization.
- [Docker container lab](https://docs.docker.com/guides/lab-container-getting-started/) — hands-on explanation of containers and how they differ from virtual machines.
- [Kubernetes documentation](https://kubernetes.io/docs/home/) — official overview of container orchestration and Kubernetes concepts.
