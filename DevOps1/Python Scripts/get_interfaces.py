import getpass
from netmiko import ConnectHandler
from tabulate import tabulate

def get_interface_details(ip_address, username, password, enable_secret):
    """
    Connects to a Cisco switch and retrieves interface details.

    Args:
        ip_address (str): The IP address of the switch.
        username (str): The SSH username.
        password (str): The SSH password.
        enable_secret (str): The enable password (if required for 'show' commands).

    Returns:
        list: A list of dictionaries, each containing interface details.
    """
    cisco_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address,
        'username': username,
        'password': password,
        'secret': enable_secret,
        'global_delay_factor': 2 # Adds slight delay to ensure commands complete
    }

    try:
        print(f"Connecting to {ip_address}...")
        net_connect = ConnectHandler(**cisco_device)
        net_connect.enable() # Enter enable mode if needed for show commands
        print("Connection successful.")

        # Execute command and parse output using TextFSM via use_textfsm=True
        # This relies on ntc-templates for the "show interface status" command
        command = "show interface status"
        output = net_connect.send_command(command, use_textfsm=True)

        net_connect.disconnect()
        return output

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def print_details(interfaces):
    """
    Prints the interface details in a structured table.
    """
    if not interfaces:
        print("No interface data retrieved.")
        return

    # Extract required fields for the table
    table_headers = ["Port", "Name/Description", "Status", "VLAN", "Duplex", "Speed", "Type"]
    table_data = []

    for intf in interfaces:
        # NTC templates field names for "show interface status"
        port = intf.get('port', 'N/A')
        name = intf.get('name', 'N/A')
        status = intf.get('status', 'N/A')
        vlan = intf.get('vlan', 'N/A')
        duplex = intf.get('duplex', 'N/A')
        speed = intf.get('speed', 'N/A')
        intf_type = intf.get('type', 'N/A')

        table_data.append([port, name, status, vlan, duplex, speed, intf_type])

    print("\n--- Interface Details ---")
    print(tabulate(table_data, headers=table_headers, tablefmt="grid"))


if __name__ == "__main__":
    # Prompt user for credentials and device IP
    ip_address = input("Enter the switch IP address: ")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    enable_secret = getpass.getpass("Enter your enable password: ")

    interface_details = get_interface_details(ip_address, username, password, enable_secret)

    if interface_details:
        print_details(interface_details)
