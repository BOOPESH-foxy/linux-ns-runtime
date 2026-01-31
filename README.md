# Ghostd (Linux Namespace Runtime)

A lightweight container runtime mimic built with Python, designed to provide Docker-like functionality using Linux namespaces.

## Features

- **Volume Management**: Create, list, and inspect persistent volumes
- **OCI Image Support**: Pull container images from Docker Hub with multi-architecture support
- **Linux Namespace Integration**: Built to leverage Linux namespaces for containerization
- **FHS Compliant**: Follows Filesystem Hierarchy Standard with data stored in `/var/lib/ghostd`

## Project Structure

```
ghostd/
├── main.py              # Main CLI entry point
├── engine/
│   └── volume.py        # Volume management functionality
├── oci_images/
│   └── pull.py          # OCI image pulling functionality
├── cargo.toml           # Project configuration and dependencies
└── README.md
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/BOOPESH-foxy/linux-ns-runtime.git
   cd linux-ns-runtime
   ```

2. **Install dependencies:**
   ```bash
   pip install requests
   ```

3. **Make the binary executable and link it:**
   ```bash
   chmod +x main.py
   sudo ln -sf $(pwd)/main.py /usr/local/bin/ghostd
   ```

4. **Initialize the directory structure:**
   ```bash
   sudo mkdir -p /var/lib/ghostd/{volumes,images,containers}
   sudo chmod 755 /var/lib/ghostd
   ```

## Usage

### Volume Management

**Create a volume:**
```bash
ghostd volume create my-volume
```

**List all volumes:**
```bash
ghostd volume list
```

**Inspect a volume:**
```bash
ghostd volume inspect my-volume
```

### Image Operations

**Pull an image from Docker Hub:**
```bash
ghostd pull ubuntu --tag latest
```

The image puller supports:
- Multi-architecture images (automatically selects linux/amd64)
- Official Docker Hub images (e.g., `ubuntu`, `nginx`)
- Custom repositories (e.g., `myuser/myimage`)

## Architecture

### Why `/var/lib/ghostd`?

- **Permissions**: Enforces proper Linux user/group permission handling
- **Persistence**: Data persists independently of source code location
- **Standards**: Follows the Filesystem Hierarchy Standard (FHS) for native Linux tool behavior

### Components

- **VolumeManager**: Handles persistent volume creation and management
- **OCI Image Puller**: Downloads and processes container images from registries
- **CLI Interface**: Provides Docker-like command structure

## Requirements

- Python 3.8+
- Linux operating system (for namespace support)
- `requests` library for HTTP operations

## Development Status

This is a work-in-progress container runtime. Current functionality includes:
- Volume management
- OCI image pulling with multi-arch support
