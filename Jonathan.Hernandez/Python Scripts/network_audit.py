import csv
from netmiko import ConnectHandler
import re
import getpass
import os

# Define the list of network devices
# You can add more devices to this list
devices = [
    {
        'device_type': 'cisco_ios',
        'host': '10.206.20.16',  # Replace with your switch's IP address
        'username': 'jhernandez', # Replace with your username or prompt later
        'password': 'Novel911Proud=', # Replace with your password or prompt later
        'secret': 'Cover-59-Clock', # Replace with your enable password
        'port': 22,
    },
    # Add more devices here if needed
    # {
    #     'device_type': 'cisco_ios',
    #     'host': '192.168.1.2',
    #     'username': 'your_username',
    #     'password': 'your_password',
    #     'secret': 'your_enable_password',
    #     'port': 22,
    # },
]

# Function to extract required information from command output
def parse_interface_details(output_status, output_details):
    # Regex to capture the required information from "show interface status"
    status_lines = output_status.strip().split('\n')
    # Skip header lines
    status_data = [re.split(r'\s{2,}', line.strip()) for line in status_lines[1:] if line.strip()]

    # Regex to capture speed and duplex from "show interface <interface> | include (Duplex|Speed)"
    details_data = {}
    for line in output_details.strip().split('\n'):
        if 'Duplex' in line or 'Speed' in line:
            parts = line.strip().split(',')
            interface_name = parts[0].split()[0]
            duplex = parts[1].strip().split(':')[1].strip()
            speed = parts[2].strip().split(':')[1].strip()
            details_data[interface_name] = {'duplex': duplex, 'speed': speed}

    parsed_data = []
    for data in status_data:
        if len(data) >= 5:
            port, name, status, vlan, duplex_status, speed_type = data[0], data[1], data[2], data[3], "N/A", "N/A"
            # Attempt to get speed and duplex details if available
            if port in details_data:
                duplex_status = details_data[port]['duplex']
                speed_type = details_data[port]['speed'] # The "type" column in show interface status usually refers to the media type, but speed and duplex are in show interface.

            parsed_data.append({
                'Port': port,
                'Name': name,
                'Status': status,
                'VLAN': vlan,
                'Duplex': duplex_status,
                'Speed/Type': speed_type, # Adjusting to include speed and type info. The original "type" column from `show interface status` can also be added.
            })
    return parsed_data

# Function to connect to a device and get data
def get_interface_info(device):
    try:
        print(f"Connecting to {device['host']}...")
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        
        # Commands to get the required information
        output_status = net_connect.send_command("show interface status")
        
        # Need to run a command to get duplex and speed details as well
        # "show interface detail" or "show interface <int>" is often needed for specific details not in "status"
        # For simplicity, we'll try a generic command to fetch duplex/speed for all interfaces
        output_details = net_connect.send_command("show interface | include (Duplex|Speed|line protocol)")
        
        net_connect.disconnect()
        print(f"Successfully gathered data from {device['host']}")
        
        parsed_data = parse_interface_details(output_status, output_details)
        for item in parsed_data:
            item['Switch_IP'] = device['host'] # Add the switch IP to the data
        return parsed_data
    except Exception as e:
        print(f"Error connecting to or gathering data from {device['host']}: {e}")
        return []

# Main execution
all_interfaces_data = []
for device in devices:
    interfaces = get_interface_info(device)
    all_interfaces_data.extend(interfaces)

# Define the CSV file path
csv_path = 'C:\\temp\\switch_port_info.csv' # Ensure the 'temp' folder exists or change path
# Or for a general path in the user's home directory
# csv_path = os.path.join(os.path.expanduser('~'), 'switch_port_info.csv')

# Export to CSV
if all_interfaces_data:
    keys = all_interfaces_data[0].keys()
    with open(csv_path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_interfaces_data)
    print(f"\nSuccessfully exported data to {csv_path}")
else:
    print("No data collected. Check connection details and error messages.")
