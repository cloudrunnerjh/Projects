from netmiko import ConnectHandler
import getpass, os
from datetime import datetime

# Ask for credentials
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")   # hidden typing
device_ips = input("Enter device IP(s), comma-separated: ")

# Split into a list (strip spaces)
device_list = [ip.strip() for ip in device_ips.split(",")]

# Commands to run on each device
commands = [
    "show version",
    "show ip interface brief",
    "show vlan brief",
]

# Create an output folder
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
outdir = f"outputs_{timestamp}"
os.makedirs(outdir, exist_ok=True)

for ip in device_list:
    print(f"\n============================")
    print(f"Connecting to {ip}...")
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
    }

    try:
        conn = ConnectHandler(**device)

        # File per device
        outfile = os.path.join(outdir, f"{ip.replace('.', '-')}.txt")
        with open(outfile, "w") as f:
            f.write(f"Device: {ip}\n")
            f.write(f"Collected on: {timestamp}\n\n")

            for cmd in commands:
                print(f"\n--- {ip}: {cmd} ---")
                output = conn.send_command(cmd)
                print(output)

                # Save to file
                f.write(f"\n--- {cmd} ---\n")
                f.write(output + "\n")

        conn.disconnect()
        print(f"\n[OK] Output saved to {outfile}\n")

    except Exception as e:
        print(f"[ERROR] Could not connect to {ip}: {e}")