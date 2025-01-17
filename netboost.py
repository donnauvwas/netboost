import os
import subprocess

def optimize_network():
    print("Starting network optimization...")

    # Disable Windows Auto-Tuning
    print("Disabling Windows Auto-Tuning...")
    subprocess.run(["netsh", "interface", "tcp", "set", "global", "autotuninglevel=disabled"], check=True)

    # Enable TCP Chimney Offload
    print("Enabling TCP Chimney Offload...")
    subprocess.run(["netsh", "int", "tcp", "set", "global", "chimney=enabled"], check=True)

    # Set TCP Receive Window Auto-Tuning Level to high
    print("Setting TCP Receive Window Auto-Tuning Level to high...")
    subprocess.run(["netsh", "int", "tcp", "set", "global", "rss=enabled"], check=True)

    # Increase TCP Window Size
    print("Increasing TCP Window Size...")
    subprocess.run(["netsh", "interface", "tcp", "set", "global", "congestionprovider=ctcp"], check=True)

    # Enable ECN Capability
    print("Enabling ECN Capability...")
    subprocess.run(["netsh", "int", "tcp", "set", "global", "ecncapability=enabled"], check=True)

    # Optimize DNS Cache
    print("Optimizing DNS Cache...")
    subprocess.run(["ipconfig", "/flushdns"], check=True)

    print("Network optimization complete!")

if __name__ == "__main__":
    optimize_network()