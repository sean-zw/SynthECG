# SynthECG Development Container

This folder contains the Docker development environment configuration for SynthECG.

## 🚀 Quick Start

1. **Prerequisites**:
   - VS Code with Dev Containers extension
   - Docker with NVIDIA Container Toolkit
   - NVIDIA GPU with CUDA support

2. **Open in container**:
   - Open this project in VS Code
   - `Ctrl+Shift+P` → "Dev Containers: Reopen in Container"
   - Wait for the container to build (first time only)

3. **Verify setup**:
   ```bash
   python --version   # Python 3.11.x
   gcc --version      # GCC 11.3.0  
   nvidia-smi         # Your GPU info
   nvcc --version     # CUDA 12.4.0
   ```

## 📦 What's Included

- **Base**: `nvidia/cuda:12.4.0-devel-ubuntu22.04`
- **Python**: 3.11 with pip and dev tools
- **Compiler**: GCC 11.3.0 for CUDA extensions
- **GPU Access**: Full NVIDIA GPU passthrough
- **Extensions**: Python, Pylance, Debugpy, GitHub Copilot

## 🛠️ Development

Once inside the container follow the [Linux setup steps](/README.md).

## 🐛 Troubleshooting

**GPU not detected?**
- Install [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)
- Restart Docker: `sudo systemctl restart docker`

**Extensions not working?**
- Rebuild container: `Ctrl+Shift+P` → "Dev Containers: Rebuild Container"

## 💡 Manual Setup

Without VS Code Dev Containers:

```bash
docker run -it --gpus all \
  -v $(pwd):/root/SynthECG \
  -w /root/SynthECG \
  nvidia/cuda:12.4.0-devel-ubuntu22.04 \
  bash
```

Then install Python 3.11, GCC 11, and project dependencies manually.