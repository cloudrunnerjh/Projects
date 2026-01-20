##############################################
# Project:        System Administration/Cheat Sheets
# File:           CUPS_Cheat_Sheet.sh
# Author:         Jonathan Hernandez
# Created:        2025-09-05
# Last Modified:  2025-09-05
# Version:        1.0
# Description:    CUPS (Common UNIX Printing System) admin & troubleshooting commands
#
# Notes:
# - Quick reference for Linux CUPS service management, logs, printers, and jobs
# - Commands are grouped by category for readability
##############################################

# ===============================
# SERVICE MANAGEMENT
# ===============================

# Check CUPS service status
sudo systemctl status cups

# Start / Stop / Restart / Reload CUPS
sudo systemctl start cups
sudo systemctl stop cups
sudo systemctl restart cups
sudo systemctl reload cups

# Enable/Disable CUPS on boot
sudo systemctl enable cups
sudo systemctl disable cups


# ===============================
# LOGGING & JOURNAL
# ===============================

# View all CUPS log entries
journalctl -u cups

# Follow logs in real-time
journalctl -u cups -f

# View logs in a specific time range
journalctl -u cups --since "2025-01-01" --until "2025-01-31"

# View logs by priority
journalctl -u cups -p err

# Logs for a specific user
journalctl -u cups _UID=$(id -u <username>)

# Logs for a specific printer
journalctl -u cups | grep "<printer_name>"

# Logs for a specific IP
journalctl -u cups | grep "<ip_address>"

# Traditional log files
sudo tail -f /var/log/cups/error_log
sudo tail -f /var/log/cups/access_log


# ===============================
# CONFIGURATION
# ===============================

# View main configuration
cat /etc/cups/cupsd.conf

# Edit main configuration
sudo nano /etc/cups/cupsd.conf

# Check CUPS version
cupsd -v


# ===============================
# PRINTERS & QUEUES
# ===============================

# List printers and their status
lpstat -p

# Show system default destination and available queues
lpstat -d

# Set default printer
lpoptions -d <printer_name>

# Add a new printer (IPP Everywhere/driverless example)
sudo lpadmin -p <printer_name> -E -v <device_uri> -m everywhere

# Remove a printer
sudo lpadmin -x <printer_name>


# ===============================
# PRINT JOBS
# ===============================

# Print a test page
lp -d <printer_name> /usr/share/cups/data/testprint

# Cancel a print job
cancel <job_id>

# Filter logs for a specific job id
journalctl -u cups -o cat | grep "Job <job_id>"


# ===============================
# QUICK TIPS
# ===============================

# Reload config without disconnecting clients
sudo systemctl reload cups

# If auth/permission errors:
#   - Check cupsd.conf 'Listen' and '<Location>' blocks
#   - Ensure clients/users are allowed

# Common Device URIs:
#   - ipp://<printer_ip>/ipp/print
#   - ipps://<printer_ip>/ipp/print
#   - lpd://<printer_ip>/queue
#   - socket://<printer_ip>:9100
#   - usb://... (local)

# Key files & dirs:
#   - /etc/cups/cupsd.conf    (daemon config)
#   - /etc/cups/printers.conf (printers)
#   - /var/log/cups/*         (logs)
#   - /var/spool/cups         (queue/spool)
