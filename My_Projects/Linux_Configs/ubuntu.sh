#Ubuntu Server Builtout Script
#Set Hostname
$ sudo hostnamectl set-hostname ubuntudesk1.corp.globomantics.local 
$ hostanmectl
#Set Timezone
$ sudo timedatectl set-timezone America/Los_Angeles
$ timedatectl
#Set Static IP Address
sudo nano /etc/netplan/01-netcfg.yaml
sudo netplan apply
#Edit DNS settings
sudo nano /etc/netplan/01-netcfg.yaml
sudo nano /etc/systemd/resolved.conf
sudo systemctl restart systemd-resolved
sudo nano /etc/NetworkManager/NetworkManager.conf
sudo systemctl restart NetworkManager
sudo nano /etc/hosts
sudo nano /etc/hostname
sudo nano /etc/nsswitch.conf
sudo nano /etc/hosts
sudo nano /etc/netplan/01-netcfg.yaml
sudo nano /etc/netplan/50-cloud-init.yaml
sudo nano /etc/netplan/01-netcfg.yaml

#sudo nano /etc/netplan/50-cloud-init.yaml
sudo nano /etc/netplan/01-netcfg.yaml

vi /etc/resolv/conf

sudo apt update

sudo apt upgrade

sudo snap refresh
sudo apt install --reinstall

sudo apt install bind9 bind9utils bind9-doc

sudo nano /etc/default/named

sudo systemctl restart bind9

sudo apt install neofetch
To have Neofetch run automatically when you log in, you can add it to your shell's startup script (e.g., ~/.bashrc or ~/.zshrc). 

nano 

sudo systemctl stop sssd
sudo systemctl disable sssd
Fix #2:

sudo cp /usr/lib/x86_64-linux-gnu/sssd/conf/sssd.conf /etc/sssd/.
sudo chmod 600 /etc/sssd/sssd.conf 
sudo systemctl enable sssd
sudo systemctl start sssd

Ubuntu
Update the instance

Copy
apt update -y
apt upgrade -y
Install Docker

Copy
sudo apt install docker.io
Install Docker Compose

Copy
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
Ensure docker-compose is executable

Copy
sudo chmod +x /usr/local/bin/docker-compose
Activate Docker

Copy
sudo systemctl enable docker
sudo systemctl start docker
Add the current user to the docker group so that you can run Docker commands without using sudo.

Copy
sudo usermod -aG docker $USER
newgrp docker

Managing the Gateway Service
The following commands can be executed to start, restart, or stop the Keeper Gateway as a service:

Copy
sudo systemctl start keeper-gateway
sudo systemctl restart keeper-gateway
sudo systemctl stop keeper-gateway

Verbose Logging
To add verbose debug logging, modify this file:

Copy
/etc/systemd/system/keeper-gateway.service
and add the -d flag to the "gateway start" command, e.g:

Copy
ExecStart=/bin/bash -c "/usr/local/bin/gateway start --service -d --config-file /etc/keeper-gateway/gateway-config.json"
Apply changes to the service:

Copy
sudo systemctl daemon-reload
sudo systemctl restart keeper-gateway

Upgrading
Executing the following command will upgrade the Keeper Gateway to the latest version: 

Copy
curl -fsSL https://keepersecurity.com/pam/install | sudo bash -s --

Linux
New Gateway
Execute the following command to download and run the KeeperPAM installer with auto update enabled. 

The --autoupdate parameter activates the auto updater in addition to the Keeper Gateway.

Copy
curl -fsSL https://keepersecurity.com/pam/install | \
  sudo bash -s -- --autoupdate
Existing Keeper Gateway
Activate the Auto Updater on an existing installation by executing the following Keeper Gateway command:

Copy
sudo keeper-gateway autoupdate enable
Verify Installation (Optional)

Verify that the Auto Updater has been installed successfully by executing the following Keeper Gateway command:

Open a terminal: 
Update the package list: sudo apt-get update 
Install the open-vm-tools packages: sudo apt-get install open-vm-tools open-vm-tools-desktop (for desktop) or sudo apt-get install open-vm-tools (for server) 
Reboot the virtual machine: sudo reboot

netbox01@odc2netbox01:~$ sudo nano /etc/resolv.conf
netbox01@odc2netbox01:~$ sudo nano /etc/nsswitch.conf

Copy
sudo keeper-gateway autoupdate status

Ubuntu Hardening with Commands & Explanations

1. Update and Clean the System
Keep the system up to date.

sudo apt update && sudo apt upgrade -y
sudo apt autoremove --purge -y
#Applies security patches and removes unused packages.

2. Create a Non-root Admin User
sudo adduser youradmin
sudo usermod -aG sudo youradmin
#Avoids using root directly, improves auditability.

3. Disable Root SSH Login & Password Auth
sudo nano /etc/ssh/sshd_config
#Update or add:

PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
Then restart SSH:

sudo systemctl restart ssh
#Secures SSH access, allowing only key-based login.

Set Up SSH Key Authentication
On your client machine:

ssh-keygen -t rsa -b 4096
ssh-copy-id youradmin@your-server-ip
#Prevents brute-force attacks by eliminating passwords.

5. Enable UFW Firewall
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
#Limits access to only essential ports.

6. Install and Configure Fail2Ban
sudo apt install fail2ban -y
sudo systemctl enable fail2ban
Optionally edit the config:

sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo nano /etc/fail2ban/jail.local
#Blocks IPs after too many failed login attempts.

7. Enable AppArmor
Check status:

sudo apparmor_status
To enforce profiles:

sudo aa-enforce /etc/apparmor.d/*
#Restricts what apps can do, using mandatory access control.

8. Remove Unused Services
List services:

sudo systemctl list-unit-files | grep enabled
Disable unused ones:

sudo systemctl disable service-name
#Reduces attack surface by turning off unnecessary services.

9. Install Rootkit Hunter & ClamAV
sudo apt install rkhunter clamav -y
sudo rkhunter --update
sudo rkhunter --check
#Detects hidden malware and rootkits.

10. Audit and Monitor with auditd
sudo apt install auditd audispd-plugins -y
sudo systemctl enable --now auditd
Edit audit rules:

sudo nano /etc/audit/rules.d/audit.rules
Example rule:

-w /etc/passwd -p wa -k passwd_changes
Apply:

sudo systemctl restart auditd
#Tracks changes and command usage for accountability.

11. Enable Automatic Security Updates
sudo apt install unattended-upgrades -y
sudo dpkg-reconfigure --priority=low unattended-upgrades
Optional config:

sudo nano /etc/apt/apt.conf.d/50unattended-upgrades
#Ensures important patches are applied without delay.

12. Enable Command Logging (Command Audit)
Append to /etc/profile:

echo 'export PROMPT_COMMAND='"'"'RETRN_VAL=$?;logger -p local6.debug "$(whoami) [$$]: $(history 1 | sed "s/^[ ]*[0-9]\+[ ]*//") [$RETRN_VAL]"'"'" | sudo tee -a /etc/profile
Edit rsyslog config:

sudo nano /etc/rsyslog.conf
Uncomment or add:

local6.*                        /var/log/cmdlog.log
Then restart rsyslog:

sudo systemctl restart rsyslog
#Logs every command users run, useful for tracking changes and breaches.

Ansible:
---
- name: Ubuntu Server Hardening Playbook
  hosts: all
  become: true

  vars:
    admin_user: youradmin
    ssh_pub_key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"  # or provide a static string

  tasks:

  - name: Update and upgrade the system
    apt:
      update_cache: yes
      upgrade: dist
      autoremove: yes

  - name: Create admin user
    user:
      name: "{{ admin_user }}"
      groups: sudo
      shell: /bin/bash
      state: present
      create_home: yes

  - name: Set authorized key for admin user
    authorized_key:
      user: "{{ admin_user }}"
      key: "{{ ssh_pub_key }}"
      state: present

  - name: Disable root SSH login and password authentication
    lineinfile:
      path: /etc/ssh/sshd_config
      regexp: "{{ item.regexp }}"
      line: "{{ item.line }}"
      state: present
    with_items:
      - { regexp: '^PermitRootLogin', line: 'PermitRootLogin no' }
      - { regexp: '^PasswordAuthentication', line: 'PasswordAuthentication no' }
      - { regexp: '^PubkeyAuthentication', line: 'PubkeyAuthentication yes' }

  - name: Restart SSH
    service:
      name: ssh
      state: restarted

  - name: Enable UFW and allow essential ports
    ufw:
      rule: allow
      port: "{{ item }}"
    with_items:
      - '22'
      - '80'
      - '443'

  - name: Set default UFW policies
    ufw:
      state: enabled
      policy: deny
      direction: incoming

  - name: Install Fail2Ban
    apt:
      name: fail2ban
      state: present

  - name: Enable Fail2Ban
    service:
      name: fail2ban
      enabled: yes
      state: started

  - name: Enforce all AppArmor profiles
    shell: "aa-enforce /etc/apparmor.d/* || true"
    args:
      warn: false

  - name: Install rootkit hunter and ClamAV
    apt:
      name:
        - rkhunter
        - clamav
      state: present

  - name: Run rkhunter update
    shell: rkhunter --update
    ignore_errors: yes

  - name: Install and enable auditd
    apt:
      name: auditd
      state: present

  - name: Enable auditd
    service:
      name: auditd
      enabled: yes
      state: started

  - name: Add audit rule for passwd changes
    copy:
      dest: /etc/audit/rules.d/passwd.rules
      content: "-w /etc/passwd -p wa -k passwd_changes"

  - name: Restart auditd
    service:
      name: auditd
      state: restarted

  - name: Enable unattended upgrades
    apt:
      name: unattended-upgrades
      state: present

  - name: Configure command auditing in /etc/profile
    lineinfile:
      path: /etc/profile
      line: 'export PROMPT_COMMAND='\''RETRN_VAL=$?;logger -p local6.debug "$(whoami) [$$]: $(history 1 | sed "s/^[ ]*[0-9]\+[ ]*//") [$RETRN_VAL]"'\'''
      state: present

  - name: Enable rsyslog command logging
    blockinfile:
      path: /etc/rsyslog.conf
      block: |
        local6.*                        /var/log/cmdlog.log

  - name: Restart rsyslog
    service:
      name: rsyslog
      state: restarted


Step-by-Step: Install Ansible on Ubuntu

🔸 1. Update your system
sudo apt update && sudo apt upgrade -y
🔸 2. Install Ansible
Ubuntu (22.04 and later) includes Ansible in its official repositories:

sudo apt install ansible -y
🔹 This will install the latest stable version from Ubuntu's repo.
For latest version from Ansible's PPA, see optional step below.
🔸 3. Verify Ansible installation
ansible --version
You should see output like:

ansible [core 2.x.x]
🗂️ Optional: Create a Simple Inventory File

Create a file called inventory with your server IP or hostname:

[ubuntu_servers]
192.168.1.100 ansible_user=youradmin ansible_ssh_private_key_file=~/.ssh/id_rsa
Replace:

192.168.1.100 with your Ubuntu server IP
youradmin with your SSH user
Adjust ~/.ssh/id_rsa if using a different SSH key
▶️ Run the Playbook

Save the playbook as ubuntu_hardening.yml, then run:

ansible-playbook -i inventory ubuntu_hardening.yml
✅ Optional: Install Latest Ansible via PPA

If you want the latest Ansible version, run:

sudo apt install software-properties-common -y
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y

 Your Datadog Agent is running and functioning properly.
  It will continue to run in the background and submit metrics to Datadog.
  If you ever want to stop the Datadog Agent, run:

      sudo systemctl stop datadog-agent

  And to run it again run:

      sudo systemctl start datadog-agent
