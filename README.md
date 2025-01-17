# NetBoost

NetBoost is a Python script designed to optimize network settings on Windows to potentially increase download and upload speeds. It modifies various TCP settings to improve network performance.

## Features

- Disables Windows Auto-Tuning to prevent unnecessary bandwidth throttling.
- Enables TCP Chimney Offload for better CPU and network performance.
- Sets TCP Receive Window Auto-Tuning Level to high to optimize data flow.
- Increases TCP Window Size using the Compound TCP (CTCP) congestion provider.
- Enables Explicit Congestion Notification (ECN) to reduce packet loss.
- Flushes the DNS cache to ensure the latest DNS settings are used.

## Requirements

- Windows operating system
- Python 3.x installed

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/netboost.git
   cd netboost
   ```

2. **Run the script as an administrator:**

   Open Command Prompt as an administrator and navigate to the directory where `netboost.py` is located, then execute:

   ```bash
   python netboost.py
   ```

3. **Follow the on-screen instructions.**

   The script will perform a series of network optimizations. You might need to restart your computer for all changes to take effect.

## Disclaimer

Use this script at your own risk. While it is designed to improve network performance, it may not be suitable for all network environments. Ensure you have the necessary permissions to modify network settings on your computer.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Make sure to run the script with administrative privileges, as modifying system network settings typically requires elevated permissions.