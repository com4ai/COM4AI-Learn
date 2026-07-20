# In-Network AI

In-network AI moves selected AI-related work from end servers into network infrastructure itself. Instead of treating the network only as a path for data, programmable switches, SmartNICs, DPUs, and network-attached accelerators can filter, aggregate, route, secure, or sometimes analyze data while it is moving.

```text
Traditional approach
AI worker ── data ── network ── data ── AI worker

In-network approach
AI worker ── data ── network device performs a limited operation ── result ── AI worker
```

## In-Network AI Versus Networking for AI

**Networking for AI** uses networks to connect AI systems: users call model APIs, servers retrieve data, and training workers exchange gradients.

**In-network AI** changes the network's role. A capable network device executes a narrowly defined operation during data movement. The goal is to reduce the traffic, latency, and CPU or GPU communication overhead that would occur if every operation happened only on end servers.

| Question | Networking for AI | In-network AI |
|---|---|---|
| **What does the network do?** | Moves data between AI components. | Moves data and performs selected operations on it. |
| **Where does computation run?** | Usually on CPUs, GPUs, or dedicated AI accelerators. | Partly on switches, DPUs, SmartNICs, or network-attached devices. |
| **Typical examples** | Model APIs, vector databases, distributed training, load balancing. | Gradient aggregation, packet filtering, telemetry analysis, traffic steering, and security offload. |
| **Main benefit** | Connects the AI system. | Reduces the work and data movement required from the AI system. |

## Why Use In-Network AI?

Modern AI clusters move enormous amounts of data. In distributed training, workers repeatedly exchange gradients. In inference platforms, requests may pass through gateways, security controls, caches, retrieval services, and model servers. When data must travel to a CPU or GPU for a simple operation and then travel back, the movement itself can become the bottleneck.

In-network AI can help by:

- **Reducing data movement** — aggregate, filter, compress, or discard data before it travels farther.
- **Lowering latency** — handle simple decisions close to the packet path.
- **Freeing host resources** — offload networking, storage, security, and communication tasks from CPUs and GPUs.
- **Improving scalability** — avoid making one host or parameter server process every update from a large group of workers.
- **Adding observability and security** — inspect traffic and enforce policy without relying only on the application server.

## Where In-Network AI Runs

| Infrastructure component | What it can do | AI-related example |
|---|---|---|
| **Programmable switch** | Perform simple, line-rate packet processing and aggregation within strict hardware limits. | Aggregate distributed-training updates as they pass through the switch. |
| **SmartNIC or SuperNIC** | Offload networking work from the host and accelerate network data paths. | Support RDMA traffic and data movement for GPU clusters. |
| **Data Processing Unit (DPU)** | Run programmable networking, storage, security, and infrastructure services on embedded CPU cores and accelerators. | Isolate tenant traffic, apply policies, or offload data-path services from AI servers. |
| **Network switch with collective offload** | Perform network-assisted reductions and multicast for collective communication. | Accelerate all-reduce operations during distributed training. |
| **Edge gateway or router** | Filter, classify, or route data close to where it is produced. | Select which sensor data should be sent to a cloud AI model. |

```text
Distributed training without in-network aggregation
Worker 1 ─┐
Worker 2 ─┼── all updates travel to endpoints ── aggregate
Worker 3 ─┘

Distributed training with in-network aggregation
Worker 1 ─┐
Worker 2 ─┼── switch aggregates updates ── smaller combined result
Worker 3 ─┘
```

## Common In-Network AI Operations

| Operation | What happens in the network | AI value |
|---|---|---|
| **Aggregation and reduction** | Combine values from multiple workers, such as sums or averages. | Reduces traffic for collective operations such as all-reduce. |
| **Filtering and sampling** | Forward only relevant records or a representative subset. | Reduces the data sent to downstream models or storage. |
| **Traffic classification and steering** | Recognize traffic properties and route requests to an appropriate service. | Directs inference traffic to the correct model, region, or accelerator pool. |
| **Caching** | Keep reusable data closer to users or services. | Reduces repeated retrieval of common model assets or responses. |
| **Security inspection and policy enforcement** | Apply network security controls before traffic reaches an AI workload. | Protects model APIs, credentials, and sensitive data. |
| **Telemetry and anomaly detection** | Collect flow statistics and detect unusual patterns. | Helps operate AI infrastructure and detect network anomalies. |

## Tools and Software

In-network AI is not usually built with a single Python library. It requires hardware support, system software, and an AI or distributed-computing framework that can use the accelerated network path.

| Layer | Tools or software | Purpose |
|---|---|---|
| **Programmable data plane** | P4 and vendor switch SDKs | Describe or program packet-processing behavior on supported switches. |
| **DPU and SmartNIC programming** | NVIDIA DOCA, Linux networking tools, DPDK | Build or deploy accelerated networking, security, and storage services. |
| **RDMA communication** | InfiniBand, RoCE, UCX, RDMA drivers | Move data with low latency and reduced CPU involvement. |
| **Distributed AI collectives** | NCCL, RCCL, MPI, UCC | Coordinate GPU or CPU workers during distributed training. |
| **Network collective offload** | NVIDIA SHARP and compatible collective libraries | Offload supported aggregation and reduction operations into the network. |
| **Orchestration and policy** | Kubernetes, CNI plugins, NetworkPolicy, service-mesh tools | Deploy, connect, secure, and observe services using the network. |

For example, NVIDIA SHARP offloads selected MPI and machine-learning collective operations from CPUs and GPUs into the network. NVIDIA documents integration through collective libraries such as NCCL, MPI, and UCC. BlueField DPUs combine a high-speed network interface with programmable Arm cores and specialized networking, storage, and security accelerators; the DOCA SDK is used to develop services for that environment.

## Limits and Challenges

In-network AI does not mean putting a full large language model inside an Ethernet switch. Network devices are designed for predictable, high-speed data-path work and have strict limits on memory, programmability, precision, and execution time.

| Challenge | Why it matters |
|---|---|
| **Limited computation and memory** | Switches and NICs can perform selected operations, not general-purpose model training or full LLM inference. |
| **Hardware dependence** | A feature may require a particular switch, DPU, NIC, driver, and software stack. |
| **Programming complexity** | Data-plane code must meet performance and safety constraints that do not apply to ordinary applications. |
| **Observability and debugging** | Failures can span hosts, drivers, switches, and distributed frameworks. |
| **Portability** | Designs tied to one vendor's offload capability may be difficult to move to another platform. |
| **Security and isolation** | Executing infrastructure functions in the network requires strong policy, access control, and update management. |

In-network AI is most valuable when an operation is simple, repeated frequently, and expensive to move between many endpoints. Complex AI reasoning and model inference normally remain on CPUs, GPUs, and dedicated accelerators.

## References

- [NVIDIA SHARP introduction](https://docs.nvidia.com/networking/display/sharpv311lts/introduction) — official description of in-network aggregation and reduction for MPI and machine-learning collectives.
- [NVIDIA SHARP Collective Library](https://docs.nvidia.com/networking/display/sharpv261/nvidia%2Bsharp%2Bcollective%2Blibrary) — integration information for MPI, NCCL, and other communication runtimes.
- [NVIDIA BlueField DPU overview](https://docs.nvidia.com/networking/display/bluefieldbmcv2601/overview) — official description of DPU networking, storage, security, and software-defined infrastructure offloads.
- [NVIDIA BlueField BSP](https://docs.nvidia.com/networking/display/bluefieldbsp453) — documentation for the BlueField software environment and DOCA framework.
- [SwitchML: Scaling Distributed Machine Learning with In-Network Aggregation](https://arxiv.org/abs/1903.06701) — research paper on programmable-switch aggregation for distributed training.
