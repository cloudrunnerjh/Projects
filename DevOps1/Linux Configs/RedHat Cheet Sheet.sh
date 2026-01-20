#Check for updates
dnf check-update

# Register the system
sudo subscription-manager register --username your_RH_username --password your_RH_password

# Attach an available subscription automatically

sudo subscription-manager attach --auto

# Check subscription status
sudo subscription-manager status

# Enable Common Repositories
# RHEL 9 uses modular repos — some are disabled by default.

sudo subscription-manager repos --list-enabled
sudo subscription-manager repos --enable codeready-builder-for-rhel-9-$(uname -m)-rpms
sudo subscription-manager repos --enable rhel-9-server-optional-rpms

# Update the System
sudo dnf update -y
sudo dnf upgrade -y

#Reboot if kernel was updated
sudo reboot

# Basic Security Hardening
# Enable & Check the Firewall

sudo systemctl enable firewalld --now
sudo firewall-cmd --state

# Common Firewall Rules
# Allow SSH

sudo firewall-cmd --permanent --add-service=ssh

# Allow HTTP & HTTPS (for web apps)
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https

# Reload firewall
sudo firewall-cmd --reload

# Enable SELinux
# RHEL 9 ships with SELinux enforcing by default — verify:

sestatus

# If it shows permissive or disabled, edit /etc/selinux/config and set:

SELINUX=enforcing

# Then:
sudo setenforce 1

#Add an Admin User & Secure SSH
# Create new admin user
sudo adduser youradmin
sudo passwd youradmin
sudo usermod -aG wheel youradmin

# Disable root SSH login (edit sshd config)
sudo nano /etc/ssh/sshd_config
# Change: PermitRootLogin no

# Restart SSH
sudo systemctl restart sshd

# Basic Audit & Security Tools

sudo dnf install -y vim wget curl net-tools tar unzip chrony
sudo dnf install -y aide  # Integrity checker

# Initialize AIDE:
sudo aide --init
sudo mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz
