# How Does Kubernetes Run AI Workloads?

Kubernetes is a platform for running containers across a group of machines. For AI, it can schedule training jobs, deploy model-inference services, attach storage for models and data, expose services to users, and recover or scale workloads when demand changes.

```text
Developer or CI system
        ↓ deploys a container image
Kubernetes control plane
        ↓ schedules Pods
CPU or GPU worker nodes
        ↓
Training job, model server, data service, or monitoring service
```

## The Basic Idea

An AI application is packaged into a **container image** that includes the application code, model runtime, and required libraries. Kubernetes runs one or more copies of that image in **Pods** on suitable cluster nodes.

```text
Container image:  model server + runtime + application code
        ↓
Pod:              one running copy of the container
        ↓
Deployment:       keeps the requested number of Pods running
        ↓
Service:          gives those Pods a stable network endpoint
```

Kubernetes does not train a model or generate responses itself. It manages the infrastructure around those activities: placement, restarts, networking, storage, configuration, permissions, and scaling.

## Core Kubernetes Objects for AI

| Kubernetes object | Role | AI example |
|---|---|---|
| **Pod** | Smallest deployable unit; runs one or more containers. | One model-inference server process. |
| **Deployment** | Maintains a desired number of interchangeable Pods and supports rolling updates. | Three replicas of a stateless text-generation API. |
| **Service** | Provides a stable address and load-balancing route to a set of Pods. | Other applications call `model-api` instead of a changing Pod IP. |
| **Job** | Runs a task to completion and retries failed Pods as configured. | A one-time embedding or model-evaluation task. |
| **CronJob** | Creates Jobs on a schedule. | Nightly data validation or model-quality report. |
| **StatefulSet** | Runs Pods with stable identities and storage relationships. | A stateful vector database or distributed training component. |
| **ConfigMap and Secret** | Provide non-sensitive configuration and sensitive values separately. | Model settings in a ConfigMap; API credentials in a Secret. |
| **PersistentVolumeClaim (PVC)** | Requests durable storage from the cluster. | Store model files, checkpoints, datasets, or a vector index. |
| **HorizontalPodAutoscaler (HPA)** | Adjusts replicas from resource or custom metrics. | Add inference Pods as request rate or queue depth increases. |

## How Kubernetes Schedules AI Workloads

The scheduler selects a node for each Pod by considering requested resources and placement rules. A Pod can request CPU, memory, GPUs, or vendor-provided extended resources.

```text
AI Pod requests:
  CPU:    4 cores
  Memory: 16 GiB
  GPU:    1

Kubernetes scheduler
        ↓
Find a healthy node with available requested resources
        ↓
Run the Pod on that node
```

For a GPU workload, the node needs the vendor driver and a compatible Kubernetes **device plugin**. The device plugin advertises GPUs as a schedulable resource—for example, `nvidia.com/gpu` on systems configured with NVIDIA's plugin. Kubernetes then places a Pod only where the requested resource is available.

Resource requests are important: they make the scheduling decision explicit and help avoid placing too many memory-intensive workloads on the same node. GPU extended resources are normally requested as whole integer devices, not fractional quantities.

## Example: API Pod Calls an Inference Pod

A simple AI application commonly has two parts:

1. An **API Pod** accepts a request from a user or web application.
2. The API Pod calls an internal **inference Pod**, which runs the model and returns a result.

```text
User or web application
        ↓ HTTP request
api-service
        ↓ routes to
API Pod
        ↓ HTTP or gRPC request
inference-service
        ↓ routes to
Inference Pod → AI model → response
        ↓
API Pod → response to user
```

Kubernetes Services give both sets of Pods stable names. The API Pod can call `inference-service` even if Kubernetes replaces or scales the inference Pods.

This simplified manifest defines the two Deployments and their internal Services. The images are placeholders; replace them with containers that implement your API and model inference.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: registry.example.com/ai-api:1.0
          ports:
            - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: api-service
spec:
  selector:
    app: api
  ports:
    - port: 80
      targetPort: 8000
  type: ClusterIP
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: inference
spec:
  replicas: 1
  selector:
    matchLabels:
      app: inference
  template:
    metadata:
      labels:
        app: inference
    spec:
      containers:
        - name: inference
          image: registry.example.com/model-inference:1.0
          ports:
            - containerPort: 8001
---
apiVersion: v1
kind: Service
metadata:
  name: inference-service
spec:
  selector:
    app: inference
  ports:
    - port: 80
      targetPort: 8001
  type: ClusterIP
```

Inside the cluster, the API code can call the inference service by name:

```python
response = requests.post(
    "http://inference-service/predict",
    json={"prompt": user_prompt},
    timeout=30,
)
```

If the inference model needs a GPU, add CPU, memory, and GPU resource requests to the **inference** container—not necessarily the API container. Kubernetes can then place the inference Pod on a GPU node while keeping the lightweight API Pod on an ordinary CPU node.

## Common Challenges

| Challenge | Good practice |
|---|---|
| **Pod remains Pending** | Inspect `kubectl describe pod`; the requested GPU, memory, node label, or storage may not be available. |
| **Pod repeatedly restarts** | Check logs, container command, memory limits, model path, and readiness configuration. |
| **Slow startup** | Cache or preload model assets carefully, reduce image size, and use readiness probes. |
| **GPU is not visible** | Verify the driver, container runtime, vendor device plugin, and requested resource name. |
| **Model data disappears** | Use durable storage for checkpoints, indexes, and data that must outlive a Pod. |
| **Sensitive values leak** | Use Secrets, least-privilege service accounts, network policy, and a secure secret-management process. |
| **Cost grows quickly** | Right-size requests, use autoscaling thoughtfully, and stop idle training or GPU workloads. |

Kubernetes makes AI operations more repeatable, but it adds operational complexity. It is most valuable when you need repeatable deployment, multiple services, resilience, scaling, or a shared compute platform—not simply because an application uses AI.

## References

- [Kubernetes: Schedule GPUs](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/) — official guide to GPU device plugins and resource requests.
- [Kubernetes: Device Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) — official explanation of vendor-specific resources such as GPUs, NICs, and FPGAs.
- [Kubernetes: Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/) — official documentation for run-to-completion workloads and parallel Jobs.
- [Kubernetes: Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) — official documentation for resource- and custom-metric scaling.
- [Kubernetes: Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) — official storage abstraction for Pods.
- [Kubernetes: Services, Load Balancing, and Networking](https://kubernetes.io/docs/concepts/services-networking/) — official networking and service-discovery concepts.
