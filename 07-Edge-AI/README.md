# Edge AI

Edge AI runs an AI model close to where data is created: on a phone, camera, robot, vehicle, factory machine, retail device, gateway, or local server. Rather than sending every input to a distant cloud service, the device performs inference locally or uses a hybrid local-and-cloud design.

```text
Cloud-only AI
Camera or device ── network ── cloud model ── network ── result

Edge AI
Camera or device ── local model ── result
                     │
                     └── optional cloud sync, update, or escalation
```

## Why Run AI at the Edge?

AI at the edge is useful when sending data to the cloud is slow, expensive, unreliable, or inappropriate.

| Benefit | Why it matters |
|---|---|
| **Low latency** | A local model can respond without waiting for a round trip to a cloud region. This matters for robotics, safety systems, interactive applications, and real-time video. |
| **Offline operation** | The device can continue working when the network is unavailable or unstable. |
| **Privacy** | Sensitive images, audio, location data, and industrial data can remain on the device. |
| **Lower bandwidth cost** | The device can send a small result or alert instead of continuous raw video, audio, or sensor data. |
| **Reliability** | Local inference avoids making every decision dependent on an external service. |
| **Personalization** | A model can adapt to a device or user while keeping the data local, when the platform supports it. |

## Common Edge AI Architecture

```text
Sensor, camera, microphone, or local data
        ↓
Preprocessing on device
        ↓
Local AI model on CPU, GPU, NPU, or accelerator
        ↓
Decision, alert, control action, or user interface
        ↓
Optional: cloud storage, analytics, model update, or human review
```

Edge AI usually performs **inference** locally. Training a large model normally happens in a data center or cloud because it needs much more data, memory, and compute. However, a device may fine-tune a small model, personalize a model, or participate in federated learning.

## Edge AI Hardware

Edge devices balance compute performance against power, size, heat, memory, and cost.

| Hardware | Typical role | Example use |
|---|---|---|
| **CPU** | Runs application logic, preprocessing, and smaller models. | A sensor gateway classifies a small set of measurements. |
| **GPU** | Provides parallel compute for vision and larger local models. | A robot processes multiple camera streams. |
| **NPU / neural engine** | Specialized low-power accelerator for neural-network inference. | A phone classifies photos or transcribes speech. |
| **Microcontroller (MCU)** | Runs compact, highly optimized models with very small memory and power budgets. | A battery-powered sensor detects an anomaly from vibration or audio data. |
| **Edge AI module or SoC** | Combines CPU, GPU, NPU, memory, I/O, and media hardware. | An embedded camera, vehicle computer, or industrial controller. |
| **Local edge server** | Runs larger models near a factory, store, hospital, or telecom site. | A local video-analysis system serves many cameras. |

Important specifications include usable memory, power consumption, thermal design, supported numeric precision, camera and sensor I/O, storage, operating system, hardware availability, and the software tools needed to deploy a model.

## Models and Optimization for Edge Devices

An edge model must fit into the device's storage and active memory, run within the latency target, and stay within its power and thermal budget. Common optimization techniques are:

| Technique | What it changes | Trade-off |
|---|---|---|
| **Quantization** | Uses lower-precision weights or activations, such as INT8. | Reduces model size, memory, and often latency; may affect accuracy. |
| **Pruning** | Removes less important model weights or structures. | Can reduce computation, but may require retraining or careful validation. |
| **Knowledge distillation** | Trains a smaller model to imitate a larger model. | Smaller and faster model, with possible quality loss. |
| **Architecture selection** | Uses an efficient model designed for mobile or embedded inference. | May give up some accuracy for speed, memory, or power efficiency. |
| **Input optimization** | Reduces image resolution, frame rate, audio length, or token context. | Lowers compute and latency but may reduce task quality. |

Optimization must be measured on the target device. A model that is fast on a desktop GPU may be slow, memory-limited, or thermally constrained on an embedded device.

## Edge AI Software and Tools

| Platform or tool | Typical deployment target | Purpose |
|---|---|---|
| **TensorFlow Lite / LiteRT** | Android, embedded Linux, and microcontroller-adjacent devices. | Optimized local inference for supported models. |
| **ONNX Runtime** | Windows, Linux, edge servers, and supported accelerators. | Portable model execution with hardware-specific execution providers. |
| **NVIDIA JetPack and TensorRT** | NVIDIA Jetson devices. | Build, optimize, and deploy AI applications on embedded NVIDIA hardware. |
| **OpenVINO** | Intel CPUs, GPUs, and supported accelerators. | Optimize and run models on Intel edge hardware. |
| **Qualcomm AI Stack and AI Hub** | Supported Snapdragon devices. | Optimize, validate, and deploy models for Qualcomm hardware. |
| **Apple Core ML and Core AI** | iPhone, iPad, Mac, and other Apple devices. | Run models on-device using the CPU, GPU, and Neural Engine. |
| **STM32Cube AI Studio / STM32Cube.AI** | STM32 microcontrollers. | Optimize, validate, and generate embedded C code for compact neural-network and machine-learning models. |
| **PyTorch ExecuTorch** | Mobile and embedded devices. | Deploy PyTorch models to constrained devices. |

## Edge AI Vendors and Ecosystems

| Vendor or ecosystem | Relevant hardware or software | Typical use |
|---|---|---|
| **NVIDIA** | Jetson modules and developer kits, JetPack, CUDA, TensorRT, DeepStream. | Robotics, computer vision, autonomous machines, and industrial edge AI. |
| **Qualcomm** | Snapdragon SoCs, Qualcomm AI Stack, AI Hub. | Mobile devices, cameras, PCs, and power-efficient embedded AI. |
| **Apple** | Apple silicon, Neural Engine, Core ML, Core AI. | Private on-device AI in Apple applications and devices. |
| **Intel** | CPUs, GPUs, edge accelerators, OpenVINO. | Edge servers, industrial systems, and Intel-based vision or analytics deployments. |
| **AMD** | Ryzen AI processors, Radeon GPUs, and embedded processors. | PCs, workstations, and embedded or industrial systems. |
| **STMicroelectronics** | STM32 microcontrollers, STM32Cube AI Studio, STM32Cube.AI (X-CUBE-AI), NanoEdge AI Studio, and selected MCUs with an embedded NPU. | TinyML and embedded AI for sensors, industrial devices, appliances, and battery-powered products. |
| **Arm ecosystem** | Arm CPUs, Mali GPUs, Ethos NPUs, and partner SoCs. | Low-power embedded devices produced by many chip and device vendors. |
| **Google and Android ecosystem** | Android AI frameworks and LiteRT. | Android phones, tablets, and embedded Android devices. |

The best platform depends on the model, operating system, target device, power budget, tools, available support, and how long the hardware must remain deployable in the field.

### STM32 and STM32Cube.AI

STM32 devices are especially useful for **TinyML**: compact models that run on microcontrollers with tightly constrained RAM, flash storage, power, and compute. Typical tasks include vibration-based anomaly detection, keyword spotting, gesture recognition, simple vision, and sensor classification.

STM32Cube.AI, also known as **X-CUBE-AI**, imports trained models from supported frameworks and generates optimized C code for inference on STM32 microcontrollers. For new projects, ST now recommends **STM32Cube AI Studio**, its newer standalone environment for model optimization, validation, performance analysis, and deployment. It builds on the STM32Cube.AI legacy and can target newer devices, including supported STM32 MCUs with the Neural-ART NPU.

```text
Trained compact model
        ↓
STM32Cube AI Studio or STM32Cube.AI
        ↓
Optimized C code and model data
        ↓
STM32 firmware
        ↓
Local inference from sensor data
```

## Edge AI Use Cases

| Area | Local AI task |
|---|---|
| **Smart cameras** | Object detection, tracking, anomaly detection, and privacy-preserving video analytics. |
| **Robotics and drones** | Navigation, obstacle detection, perception, and local control. |
| **Manufacturing** | Visual inspection, fault detection, predictive maintenance, and worker-safety monitoring. |
| **Retail** | Shelf analysis, queue estimation, inventory tracking, and loss-prevention signals. |
| **Healthcare devices** | Sensor analysis, imaging assistance, and local data processing under appropriate clinical and regulatory controls. |
| **Vehicles** | Driver assistance, sensor fusion, cabin monitoring, and local perception. |
| **Phones and computers** | Speech recognition, image enhancement, translation, accessibility, and personal AI features. |

## Challenges and Good Practices

| Challenge | Good practice |
|---|---|
| **Limited memory and storage** | Choose a model that fits with operational headroom; quantize and test it on the target. |
| **Heat and battery use** | Measure sustained performance, not only short benchmarks; design for throttling and power limits. |
| **Model updates** | Version, sign, validate, and roll back models safely. |
| **Security** | Protect device access, model files, credentials, data, and update channels. |
| **Accuracy drift** | Monitor outcomes, collect permitted feedback, and reevaluate the model as conditions change. |
| **Hardware diversity** | Define supported devices and test each model/runtime combination. |
| **Cloud dependence** | Identify which features must remain available offline and design a clear fallback path. |

Edge AI is not a replacement for cloud AI. It is a design choice: put each part of the workload where it best meets the requirements for latency, privacy, cost, connectivity, and compute.

## References

- [NVIDIA Jetson FAQ](https://developer.nvidia.com/embedded/faq) — official overview of Jetson and the JetPack edge-AI software stack.
- [OpenVINO documentation](https://docs.openvino.ai/) — official documentation for model optimization and inference on Intel hardware.
- [Apple Core ML](https://developer.apple.com/documentation/CoreML) — official documentation for on-device machine learning.
- [Apple Core AI](https://developer.apple.com/core-ai/) — official documentation for running AI models locally on Apple silicon.
- [STM32Cube.AI](https://stm32ai.st.com/stm32-cube-ai/) — official STM32 tool for optimizing and deploying trained models on STM32 microcontrollers.
- [STM32Cube AI Studio](https://www.st.com/content/st_com/en/campaigns/edge-ai-toolchain-for-mcus-z14.html) — ST's newer standalone environment for STM32 model optimization, validation, and deployment.
- [ST Edge AI tools](https://www.st.com/content/st_com/en/st-edge-ai-suite/tools.html) — official overview of ST's embedded-AI toolchain, including NanoEdge AI Studio.
- [Qualcomm AI Hub](https://aihub.qualcomm.com/) — platform for optimizing and deploying models on supported Qualcomm devices.
- [ONNX Runtime](https://onnxruntime.ai/docs/) — official documentation for cross-platform ONNX model inference.
- [TensorFlow Lite / LiteRT](https://ai.google.dev/edge/litert) — official documentation for on-device model inference.
- [ExecuTorch](https://docs.pytorch.org/executorch/stable/) — official PyTorch framework for edge deployment.
