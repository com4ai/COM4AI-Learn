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
- [NVIDIA HGX AI Factory components](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/components.html) — current examples of HBM capacity and bandwidth in AI systems.
