# Ghostd (Linux Namespace Runtime)

A lightweight container runtime mimic built with Python.

## Installation
1. Clone the repo.
   ```bash
    git clone https://github.com/BOOPESH-foxy/linux-ns-runtime.git
2. Link the binary:
   ```bash
   chmod +x main.py
   sudo ln -sf $(pwd)/main.py /usr/local/bin/ghostd
3. Initialize the directory
    ```bash
    sudo mkdir -p /var/lib/ghostd/{volumes,images,containers}
    sudo chmod 755 /var/lib/ghostd
---

### **Why use `/var/lib`?**
* **Permissions:** It forces you to handle Linux user/group permissions properly (Root vs. User).
* **Persistence:** Your data isn't tied to your `git clone` location. You can delete the source code, reinstall it, and your volumes will still be there.
* **Standards:** Following the **Filesystem Hierarchy Standard (FHS)** makes your tool feel like a native Linux utility.


### **Next Step**
Now that the path is set to `/var/lib/ghostd`