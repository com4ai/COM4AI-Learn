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

## Vendors in the In-Network AI Market

The in-network AI market includes several layers: DPU and SmartNIC vendors, switch and Ethernet-fabric vendors, accelerator vendors, and server vendors that combine these components into deployable systems. Product availability and specifications change quickly, so use this as a map of the ecosystem rather than a procurement guide.

| Vendor or ecosystem | Relevant products or technologies | Role in in-network AI |
|---|---|---|
| **NVIDIA Networking** | BlueField DPUs and SuperNICs, ConnectX NICs, InfiniBand, Spectrum Ethernet, SHARP, DOCA, NCCL. | Provides DPU-based infrastructure offload, RDMA networking, and in-network collective reduction for GPU AI clusters. |
| **AMD Pensando** | Pensando DPUs, Pollara AI NIC, P4-programmable data paths, Pensando software. | Provides programmable Ethernet data paths for AI-cluster front-end networking, storage, security, observability, and traffic offload. AMD publishes up to 400 Gb/s for the Pollara 400 AI NIC. |
| **Intel and Altera** | Intel IPUs, Ethernet adapters, FPGA IPUs, P4, DPDK, and IPDK. | Offers infrastructure offload and programmable networking for cloud and AI environments; Intel's E2100 IPU supports up to 200 GbE, while FPGA IPUs target programmable data paths. |
| **Broadcom** | Ethernet switching silicon, AI Ethernet NICs, PCIe switches, and high-radix data-center fabric technologies. | Supplies components used by many system vendors to build large Ethernet AI fabrics and scale-up or scale-out connectivity. |
| **Arista, Cisco, HPE Aruba, and other network-system vendors** | Data-center Ethernet switches, network operating systems, telemetry, routing, and automation. | Build and operate the network fabric around AI servers; some platforms integrate or support programmable services and DPU-based designs. |
| **Server and cloud providers** | AI servers, rack-scale systems, managed network fabrics, and cloud networking services. | Integrate NICs, DPUs, switches, accelerators, storage, and orchestration into an operational AI platform. |

When comparing vendors, evaluate more than port speed. Important questions include:

| Area | What to evaluate |
|---|---|
| **Programmability** | Can the data path be programmed with P4, a DPU SDK, FPGA logic, or supported APIs? |
| **Offload capabilities** | Which networking, storage, security, telemetry, RDMA, or collective operations can move off the host? |
| **AI-framework integration** | Does the platform work with NCCL, RCCL, MPI, UCX, Kubernetes, and the chosen accelerator stack? |
| **Fabric and topology** | Does it support InfiniBand, Ethernet, RoCE, Ultra Ethernet, or the topology needed by the cluster? |
| **Performance** | Compare usable bandwidth, latency, congestion management, packet-processing capacity, and CPU overhead—not only a headline link speed. |
| **Operations** | Consider drivers, observability, security isolation, upgrades, support, and interoperability with existing hardware. |

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
- [AMD Pensando DPU Technology](https://www.amd.com/en/products/data-processing-units/pensando.html) — official overview of AMD Pensando programmable DPUs for AI-cluster networking and infrastructure offload.
- [AMD Pensando Pollara 400 AI NIC](https://www.amd.com/en/products/network-interface-cards/pensando.html) — official product overview of the P4-programmable 400 Gb/s AI networking interface card.
- [Intel Infrastructure Processing Unit](https://www.intel.com/content/www/us/en/products/details/networking/ipu.html) — official overview of IPU networking, infrastructure offload, and AI infrastructure use cases.
- [Altera FPGA Infrastructure Processing Unit](https://www.intel.com/content/www/us/en/products/details/fpga/platforms/ipu.html) — official description of FPGA-based programmable IPUs for AI, RDMA, and infrastructure workloads.
- [Broadcom Networking for AI Clusters](https://www.broadcom.com/topics/what-is-networking-for-ai) — overview of AI Ethernet fabrics and high-radix networking.
- [SwitchML: Scaling Distributed Machine Learning with In-Network Aggregation](https://arxiv.org/abs/1903.06701) — research paper on programmable-switch aggregation for distributed training.
