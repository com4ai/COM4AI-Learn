# What Are AI Accelerators?

An **AI accelerator** is hardware designed to perform AI calculations more efficiently than a general-purpose CPU. It does not replace the CPU completely. Instead, the CPU usually runs the operating system, coordinates the application, prepares data, and sends the most demanding mathematical work to the accelerator.

```text
Application and CPU
        ↓
AI framework and runtime
        ↓
AI accelerator performs model calculations
        ↓
Prediction, generated text, image, or other output
```

AI accelerators are especially useful for the repeated matrix, tensor, and vector operations used in neural networks. They may be designed for model training, inference, or both.

## Why Do AI Systems Use Specialized Accelerators?

Deep-learning models repeatedly multiply large arrays of numbers and apply the same operations across many values. A CPU can perform this work, but it is designed to be flexible and to run many different kinds of programs.

An accelerator makes trade-offs. It supports a narrower set of operations or numerical formats so it can provide more parallel computation, higher memory bandwidth, lower latency, better energy efficiency, or a lower cost for a particular AI workload.

```text
CPU: flexible control, application logic, data preparation
        ↓ offload AI-heavy operations
Accelerator: repeated tensor and matrix calculations
```

## Common Types of AI Accelerators

The terms below describe **architectures or categories**. A company may use its own product name for one of these categories.

GPUs are intentionally covered in the separate [How Do GPUs Accelerate AI?](../02-How-do-GPUs-Accelerate-AI/README.md) lesson.

| Accelerator type | Main idea | Strength | Example organizations or products |
|---|---|---|---|
| **TPU** | A specialized ASIC emphasizes large matrix multiply-and-accumulate operations. | Efficient large-scale machine-learning training and inference. | Google Cloud TPU |
| **NPU** | A small, power-efficient neural-processing block is integrated into a device or system-on-chip. | On-device AI with low power use. | Phone, PC, and edge-device NPUs |
| **ASIC** | A chip is built for a defined AI purpose rather than general computing. | High efficiency for the target workload. | AWS Trainium and Inferentia |
| **FPGA** | Reconfigurable hardware is programmed after manufacturing. | Can be adapted to custom pipelines, low latency, and edge systems. | AMD Versal AI Edge and other FPGA platforms |
| **IPU** | Many independent processing tiles combine compute with local memory. | Fine-grained parallelism and flexible computational graphs. | Graphcore Intelligence Processing Unit (IPU) |
| **Wafer-scale engine** | A processor is built from an entire silicon wafer rather than a conventional chip. | Very large on-chip compute and memory for large models. | Cerebras Wafer-Scale Engine |
| **Dataflow accelerator** | Hardware and software are organized around a predictable stream of operations. | Low-latency, high-throughput inference for suitable models. | Groq Language Processing Unit (LPU) |

These categories overlap. For example, a TPU is an ASIC, and some FPGAs also include dedicated AI-engine blocks.

## How an AI Accelerator Works

Most accelerators follow the same high-level pattern:

```text
Model and input data
        ↓
Compiler or runtime chooses supported operations
        ↓
Accelerator performs parallel mathematical operations
        ↓
Results return to application or next model layer
```

The framework does not usually send ordinary Python statements directly to the hardware. It converts model operations into an optimized execution plan. This is why the compiler, runtime, libraries, and drivers are as important as the chip itself.

## Tensor Processing Units (TPUs)

A **Tensor Processing Unit (TPU)** is Google's application-specific integrated circuit (ASIC) for machine learning. TPUs are designed for large matrix operations, especially multiply-and-accumulate calculations used in neural networks.

```text
Input matrix × weight matrix
        ↓
many multiply-and-accumulate operations
        ↓
output matrix
```

Google Cloud TPUs use matrix-multiply units arranged as **systolic arrays**. Data flows across the array, allowing many multiply-and-accumulate operations to happen together. TPUs are commonly accessed through Google Cloud, and programs are compiled for them by XLA.

## Neural Processing Units (NPUs)

An **NPU** is usually an AI accelerator integrated into a laptop, phone, edge device, or system-on-chip. NPUs are designed to run AI tasks locally with low power consumption.

```text
Camera, microphone, or local application
        ↓
NPU runs a compact AI model
        ↓
Local result without sending all data to the cloud
```

Common uses include image enhancement, speech recognition, background effects, object detection, and small language-model inference. NPUs are useful when battery life, privacy, latency, or offline operation matters.

## Application-Specific AI Chips

An **ASIC** is hardware designed for a specific purpose. In AI, cloud providers and hardware companies use ASICs to optimize either training, inference, or both.

| Example | Primary focus | Key idea |
|---|---|---|
| **AWS Trainium** | Training and serving | AWS-designed AI chip for training and generative-AI workloads. |
| **AWS Inferentia** | Inference | AWS-designed chip optimized for deploying deep-learning and generative-AI models. |
| **Google TPU** | Training and inference | Matrix-processing ASIC used through Google Cloud. |

ASICs can be efficient because the hardware and software are designed together. The trade-off is that code may need a specific compiler, runtime, cloud service, or supported set of operations.

## Field-Programmable Gate Arrays (FPGAs)

An **FPGA** can be reconfigured after it is manufactured. Instead of using a fixed set of processor cores, developers configure logic blocks and data paths for a specific task.

```text
Trained model
        ↓
Compile and configure FPGA logic
        ↓
Custom low-latency inference pipeline
```

FPGAs are useful for edge AI, industrial systems, networking, video processing, and real-time inference. They can be power-efficient and adaptable, but development is more specialized than using a standard machine-learning framework. Modern FPGA-based platforms can also include dedicated AI-engine tiles.

## Graphcore Intelligence Processing Units (IPUs)

Yes—**Graphcore** is an important example of a specialized AI-accelerator approach. Its **Intelligence Processing Unit (IPU)** is a highly parallel processor built for machine learning and computational graphs.

An IPU is made of many independent **tiles**. Each tile has compute resources and its own local memory. The tiles communicate through a fast on-chip exchange fabric.

```text
Many IPU tiles
├── local compute
├── local memory
└── fast tile-to-tile communication
        ↓
parallel execution of a machine-learning graph
```

This design emphasizes fine-grained independent processing and local memory close to the computation. Graphcore software, such as the Poplar SDK, compiles and runs supported models on IPU hardware.

## Other Specialized Architectures

### Cerebras Wafer-Scale Engine

Cerebras uses a **wafer-scale engine**, meaning the processor is manufactured from an entire silicon wafer instead of being cut into many conventional chips. The goal is to place a very large amount of compute and on-chip memory in one device and reduce some communication overhead for large AI workloads.

### Groq Language Processing Unit

Groq uses the term **Language Processing Unit (LPU)** for an inference-focused accelerator. It uses a dataflow-oriented approach intended to provide predictable, low-latency execution for supported AI models.

### Edge AI Accelerators

Small accelerators can be integrated into cameras, robots, cars, gateways, and embedded devices. These systems often prioritize low power, real-time response, small physical size, and local data processing over maximum data-center throughput.

## Training and Inference

| Task | What the hardware must do | Common accelerator choices |
|---|---|---|
| **Training** | Store model weights and intermediate data, calculate gradients, and update weights repeatedly. | TPUs, training ASICs, IPUs, wafer-scale systems |
| **Inference** | Run a trained model efficiently to produce predictions or generated output. | NPUs, inference ASICs, FPGAs, dataflow accelerators |

The same accelerator can sometimes do both tasks. The best choice depends on the model, batch size, latency target, software support, available memory, power budget, and cost.

## How to Choose an AI Accelerator

Ask these questions before choosing hardware:

1. **Are you training a model or only running inference?**
2. **Does the model fit in the available memory?**
3. **Do you need low latency, high throughput, low power, or all three?**
4. **Will the model run locally, at the edge, or in the cloud?**
5. **Does your framework support the accelerator well?**
6. **Do you need a flexible platform, or is the workload stable enough for specialized hardware?**

For most learners, a hosted AI service is the simplest place to start. Specialized accelerators become more valuable when you need to reduce cost, latency, power consumption, or time-to-train at scale.

## Key Takeaways

- AI accelerators are hardware designed to speed up AI calculations that would be slower or less efficient on a CPU.
- TPUs, NPUs, ASICs, FPGAs, IPUs, wafer-scale engines, and dataflow accelerators make different hardware trade-offs.
- Graphcore's IPU is a specialized architecture with many processing tiles and local memory.
- Hardware choice must include software, memory, latency, power, cost, and the specific AI workload.

## References

- [Google Cloud TPU architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm) — official explanation of TPUs, matrix-multiply units, systolic arrays, and TPU system design.
- [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu) — official overview of TPU compilation and scaling.
- [Graphcore IPU Programmer's Guide](https://docs.graphcore.ai/projects/ipu-programmers-guide/en/latest/about_ipu.html) — official overview of IPU tiles, local memory, and the exchange fabric.
- [AWS Trainium and Inferentia](https://aws.amazon.com/ai/machine-learning/trainium/getting-started/) and [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/) — official resources for AWS purpose-built AI chips and the Neuron software stack.
- [AMD Versal AI Edge documentation](https://docs.amd.com/r/en-US/ds955-xqr-versal-ai-edge/Compute-and-Acceleration) — official example of programmable logic and AI-engine tiles for edge workloads.
- [Cerebras investor materials](https://investors.cerebras.ai/static-files/ee277690-ec46-4a23-8439-53f0816bf7d5) — description of the wafer-scale-engine approach.
- [Groq LPU architecture](https://home.cloud.groq.io/lpu-architecture) — official overview of Groq's inference-focused LPU approach.
