"""Script that handles the volumes - ghostd"""

import os
import sys


class VolumeManager:

    def __init__(self):
        self.ghostd_path = '/var/lib/ghostd/volumes'

        if not os.path.exists(self.ghostd_path):
            try:
                os.makedirs(self.ghostd_path, exist_ok=True)
            
            except PermissionError:
                print(f"[!] Critical: Cannot write to {self.ghostd_path}.")
                print("    Please run: sudo mkdir -p /var/lib/ghostd/volumes && sudo chown -R $USER /var/lib/ghostd")
                sys.exit(1)

    def create_volume(self, name):
        """Creates a directory for a named volume."""
        vol_path = os.path.join(self.ghostd_path, name)
        
        if os.path.exists(vol_path):
            print(f"[!] Error: Volume '{name}' already exists.")
            return

        os.makedirs(vol_path)
        print(f"[+] Volume '{name}' created successfully.")
        print(f"    Location: {vol_path}")

    def list_volumes(self):
        """Lists all directories in the volumes path."""
        try:
            volumes = os.listdir(self.ghostd_path)
            if not volumes:
                print("No volumes found.")
                return
            
            print(f"{'VOLUME NAME':<20} {'LOCATION'}")
            for v in volumes:
                print(f"{v:<20} {os.path.join(self.ghostd_path, v)}")
        except FileNotFoundError:
            print("Storage not initialized. Create a volume first.")

    def inspect_volume(self, name):
        vol_path = os.path.join(self.ghostd_path, name)
        if os.path.exists(vol_path):
            print(f"Volume: {name}")
            print(f"Mountpoint: {vol_path}")
        else:
            print(f"[!] Volume '{name}' not found.")