# Memory for AI

Memory determines what an AI system can hold close to its processors and how quickly it can access the data it needs. AI applications use memory for model weights, input data, intermediate calculations, prompts, generated tokens, and cached results.

```text
Storage holds data and model files
        ↓
RAM and GPU memory hold active data
        ↓
CPU or accelerator performs calculations
        ↓
Cache keeps frequently reused results close by
```

## Why Memory Matters for AI

An AI processor cannot calculate with data that it cannot access. Even a powerful CPU, GPU, or accelerator may spend time waiting if model weights or input data arrive too slowly. This is called being **memory-bound**: performance is limited by moving data rather than by mathematical computation.

Three memory properties are especially important:

| Property | Meaning | Why it matters for AI |
|---|---|---|
| **Capacity** | How much data fits in memory. | The model, input, intermediate data, and cache must fit. |
| **Latency** | How long it takes to begin a memory access. | Low latency helps small, irregular, and real-time operations respond quickly. |
| **Bandwidth** | How much data can be transferred per second. | High bandwidth feeds many parallel AI calculations with weights and activations. |

Latency and bandwidth are different. A memory system can transfer a large amount of data each second but still take time before a particular access begins. AI workloads need a suitable balance of both.

```text
Latency:   request data ───── wait ───── first byte arrives
Bandwidth: many bytes ─────────────────────────────→ per second
```

## The AI Memory Hierarchy

Memory closer to the processor is usually faster but smaller and more expensive. Memory farther away is usually larger but slower.

```text
Closest and fastest
├── registers and on-chip SRAM
├── processor cache
├── system RAM or GPU memory
├── SSD or other persistent storage
└── remote storage or another server
Largest and slowest
```

An AI system moves data between these levels. For example, it may load a model from storage into RAM, transfer model data to GPU memory, then repeatedly use small pieces of data from on-chip cache during calculations.

## Memory Technologies Used by AI Systems

| Technology | Where it is commonly used | Main characteristic |
|---|---|---|
| **SRAM** | Processor caches and on-chip accelerator memory. | Very fast and low latency, but expensive and limited in capacity. |
| **DDR or LPDDR DRAM** | System RAM in servers, desktops, laptops, and devices. | General-purpose working memory for applications, data preparation, and CPU workloads. |
| **GDDR** | Many workstation and consumer graphics cards. | High-throughput graphics memory that can also support AI workloads. |
| **HBM** | High-end AI accelerators and data-center GPUs. | Stacked memory located close to the processor, designed for very high bandwidth. |
| **SSD or other storage** | Model files, datasets, checkpoints, and logs. | Persistent and high capacity, but much slower than active memory. |

**High-Bandwidth Memory (HBM)** is important for modern AI because large models repeatedly read weights and intermediate data. HBM uses vertically stacked memory dies and a very wide connection to the accelerator, providing much higher bandwidth than ordinary system RAM. HBM is common in data-center AI hardware, while DDR, LPDDR, and GDDR remain common in other systems.

## Memory Vendors and AI-Focused Specifications

Memory manufacturers build the DRAM and HBM packages, while GPU and accelerator vendors integrate those packages into complete AI systems. When comparing memory for AI, distinguish the specification of **one HBM stack** from the total memory capacity and bandwidth of an entire GPU or server.

The three major suppliers of HBM for AI systems are **SK hynix**, **Samsung**, and **Micron**. Their products evolve quickly, but the following published HBM3E examples show the kind of specifications to compare:

| Vendor | Representative HBM product | Example published specifications | Why it matters for AI |
|---|---|---|---|
| **SK hynix** | HBM3E | 12-layer stack with 36 GB capacity; its 8-layer HBM3E has a published bandwidth of up to 1.18 TB/s. | Higher-capacity stacks help fit larger models and longer contexts close to the accelerator. |
| **Samsung** | HBM3E 12H | 36 GB capacity, 12 stacked layers, and up to 1,280 GB/s bandwidth. | High capacity and bandwidth reduce the need to move model data to slower memory. |
| **Micron** | HBM3E | 24 GB (8-high) or 36 GB (12-high), more than 1.2 TB/s bandwidth, and data rates above 9.2 Gb/s per pin. | High bandwidth keeps parallel accelerator cores supplied with model weights and activations. |

These numbers describe a memory package, not the complete accelerator. A GPU can contain several HBM stacks, so its total memory and aggregate bandwidth are much larger. For example, a system-level product specification may report the GPU's total HBM capacity, aggregate bandwidth, compute performance, interconnect, cooling, and power requirements.

When selecting an AI memory system, compare these specifications:

| Specification | Question to ask | AI impact |
|---|---|---|
| **Memory generation** | Is it DDR, LPDDR, GDDR, HBM3E, HBM4, or another technology? | Newer HBM generations generally target higher bandwidth and capacity for accelerators. |
| **Capacity** | How many GB are available per stack and per accelerator? | Determines whether model weights, activations, and the KV cache fit. |
| **Bandwidth** | How many GB/s or TB/s can the memory deliver? | Influences training throughput and token-generation speed for memory-bound models. |
| **Data rate** | How many Gb/s can each pin transfer? | Contributes to the maximum bandwidth of the memory interface. |
| **Stack height and density** | How many memory dies are stacked, and what is the capacity of each die? | Enables more capacity near the processor without expanding the board area. |
| **Power and thermals** | What energy and cooling requirements does the memory add? | Affects operating cost, density, and sustained performance in data centers. |
| **Reliability features** | Which error detection, correction, and validation features are supported? | Important for long-running training and production inference. |

Vendor specifications should be read alongside the accelerator and server documentation: a memory package can be fast, but the final AI system is also limited by the processor, interconnect, software, power, and cooling design.

## Memory Access During AI Workloads

Different AI tasks stress memory in different ways:

| Workload | Important memory use |
|---|---|
| **Training** | Stores weights, activations, gradients, optimizer state, and batches of training data. |
| **LLM inference** | Reads model weights repeatedly and stores the prompt and generated-token context in a key-value cache. |
| **Computer vision** | Moves image batches and intermediate feature maps through memory. |
| **Retrieval-augmented generation** | Keeps embeddings and retrieved documents available for search and model input. |
| **Edge AI** | Favors compact models and low-power memory because capacity and energy are limited. |

## Common Memory Challenges

| Challenge | Effect on an AI system |
|---|---|
| **Not enough capacity** | The model or training workload cannot fit; the program may fail with an out-of-memory error. |
| **Low memory bandwidth** | The processor waits for weights or activations, reducing throughput. |
| **High access latency** | Small or irregular operations respond more slowly. |
| **CPU-to-accelerator transfer** | Moving data between system RAM and GPU or accelerator memory can become a bottleneck. |
| **Large context or batch size** | More tokens, images, or examples increase active-memory requirements. |
| **Memory cost and power** | High-capacity, high-bandwidth memory increases system cost, energy use, and cooling needs. |

Common responses include using a smaller or quantized model, reducing batch size or context length, caching reused data, using a larger-memory accelerator, or distributing a model across multiple devices.

Understanding RAM, VRAM, storage, caching, latency, and bandwidth helps you choose suitable hardware, estimate whether a model will fit, and diagnose slow or failed AI workloads.

## References

- [NVIDIA GPU Performance Background](https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html) — official explanation of GPU memory hierarchy and bandwidth.
- [NVIDIA Grace Performance Tuning Guide](https://docs.nvidia.com/dccpu/grace-perf-tuning-guide/os-settings.html) — official discussion of memory locality, bandwidth, and latency considerations.
- [Micron High-Bandwidth Memory](https://www.micron.com/products/memory/hbm) — overview of HBM for AI training and inference.
- [SK hynix HBM3E design overview](https://news.skhynix.com/rulebreakers-revolutions-design-scheme-elevates-hbm3e/) — published HBM3E stack and bandwidth information.
- [Samsung HBM3E 12H announcement](https://news.samsung.com/global/samsung-develops-industry-first-36gb-hbm3e-12h-dram) — published 36 GB and 1,280 GB/s HBM3E specifications.
- [Micron HBM3E](https://www.micron.com/products/memory/hbm/hbm3e) — published HBM3E capacity, bandwidth, and data-rate specifications.
- [NVIDIA HGX AI Factory components](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/components.html) — current examples of HBM capacity and bandwidth in AI systems.
