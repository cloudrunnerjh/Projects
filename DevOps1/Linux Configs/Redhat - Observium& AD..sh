# Part 1 – Prepare Red Hat 9 on VMware
# Before we install Observium, let’s make sure your RHEL 9 is fully registered, updated, and ready.
# 1.1 Register RHEL 9
sudo subscription-manager register
sudo subscription-manager attach --auto
sudo subscription-manager repos --enable rhel-9-server-rpms
sudo subscription-manager repos --enable rhel-9-server-optional-rpms
sudo subscription-manager repos --enable rhel-9-server-extras-rpms

# 1.2 Update System & Install Essentials
sudo dnf update -y
sudo dnf install -y vim wget curl net-tools chrony firewalld unzip
sudo systemctl enable --now chronyd

#1.3 Security Baseline
#Enable Firewall:
systemctl enable firewalld --now
firewall-cmd --permanent --add-service=ssh
firewall-cmd --reload

#1.4 Verify SELinux is in enforcing mode:
getenforce

#If not, set in /etc/selinux/config:
SELINUX=enforcing

#1.5 Package & Service Management
#Remove unnecessary services (depends on role, but generally safe to disable):
systemctl disable --now avahi-daemon
systemctl disable --now cups
systemctl disable --now bluetooth
systemctl disable --now rpcbind
systemctl disable --now nfs-server
systemctl disable --now telnet.socket
#(Keep only what the server needs — e.g., SSH, firewalld, systemd-journald.)

#1.6 Install only needed packages:
dnf groupinstall "Minimal Install"

#1.7 Updates & Patching
#Enable automatic updates:
dnf install dnf-automatic -y

#1.8 Configure /etc/dnf/automatic.conf then enable timer:
systemctl enable --now dnf-automatic.timer

#1.9 System Logging & Auditing
#Enable audit logs:
dnf install audit -y
systemctl enable --now auditd

#Periodic integrity checks (AIDE):
dnf install aide -y
aide --init
mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz

#Network & Access Security
#Fail2Ban (SSH brute-force protection):
dnf install fail2ban -y
systemctl enable --now fail2ban

#Sysctl hardening (in /etc/sysctl.d/99-sysctl.conf):
net.ipv4.conf.all.rp_filter=1
net.ipv4.conf.default.rp_filter=1
net.ipv4.tcp_syncookies=1
net.ipv4.icmp_echo_ignore_broadcasts=1
net.ipv4.icmp_ignore_bogus_error_responses=1

#Apply changes:
sysctl -p
#Add user to admin group:
usermod -aG wheel itadmin
#Monitoring & Maintenance
#Resource monitoring:
dnf install sysstat -y
systemctl enable --now sysstat

#Log management:
#Journald rotates automatically; configure limits in /etc/systemd/journald.conf.

# Part 2 – Join RHEL 9 to Active Directory (randa.local)
# We’ll use SSSD + Realmd for easy domain join.
# 2.1 Install AD Integration Packages
sudo dnf install -y realmd sssd sssd-tools oddjob oddjob-mkhomedir adcli samba-common-tools krb5-workstation

# 2.2 Discover Your Domain
realm discover randa.local

# You should see your AD domain info.
# 2.3 Join Domain
sudo realm join --user=administrator randa.local

# Replace administrator with your domain admin account.
# You’ll be prompted for the AD password.

# 2.4 Configure SSSD to Allow AD Logins
sudo realm permit --all
sudo systemctl restart sssd

# 2.5 Test Domain Login
id administrator@randa.local

# You should see UID/GID mapping from AD.

# Part 3 – Install Observium on RHEL 9
# Observium requires PHP, Apache, MariaDB, and SNMP.

# 3.1 Install Dependencies
sudo dnf install -y httpd mariadb-server mariadb php php-cli php-mysqlnd php-snmp php-gd net-snmp net-snmp-utils rrdtool fping git unzip

# 3.2 Enable & Start Services
sudo systemctl enable --now httpd mariadb snmpd

# 3.3 Secure MariaDB
sudo mysql_secure_installation

# Set root password
# Remove anonymous users
# Disallow remote root login
# Remove test DB
# Reload privileges
# 3.4 Create Observium DB
sudo mysql -u root -p
CREATE DATABASE observium DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
GRANT ALL PRIVILEGES ON observium.* TO 'observium'@'localhost' IDENTIFIED BY 'StrongPasswordHere';
FLUSH PRIVILEGES;
EXIT;

# 3.5 Download & Install Observium (Community Edition)
cd /opt
sudo wget http://www.observium.org/observium-community-latest.tar.gz
sudo tar zxvf observium-community-latest.tar.gz
sudo mv observium observium
sudo mkdir -p /opt/observium/{logs,rrd}

# 3.6 Configure Observium
cd /opt/observium
cp config.php.default config.php
nano config.php

#Set DB username, password, and path to rrd & logs.
#Example:
    $config['db_host'] = 'localhost';
    $config['db_user'] = 'observium';
    $config['db_pass'] = 'StrongPasswordHere';
    $config['db_name'] = 'observium';
    $config['rrd_dir'] = '/opt/observium/rrd';
    $config['log_dir'] = '/opt/observium/logs';

# 3.7 Initialize DB
php includes/sql-schema/update.php

# 3.8 Configure Apache for Observium
sudo tee /etc/httpd/conf.d/observium.conf <<EOF
<VirtualHost *:80>
    DocumentRoot /opt/observium/html/
    <Directory "/opt/observium/html/">
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
EOF

# Set proper permissions
sudo systemctl restart httpd

# 3.9 Add Admin User
cd /opt/observium
php adduser.php admin StrongPasswordHere 10

#3.10 Schedule Discovery & Polling
sudo tee /etc/cron.d/observium <<EOF
33  */6   * * *   root    /opt/observium/discovery.php -h all >> /dev/null 2>&1
*/5 *     * * *   root    /opt/observium/poller-wrapper.py 4 >> /dev/null 2>&1
EOF

#Part 4 – Firewall Rules
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --add-service=https --permanent
sudo firewall-cmd --add-service=snmp --permanent
sudo firewall-cmd --reload

# Part 5 – Access the Web Interface
# pen in a browser:
# http://10.110.10.55
# Login with the Observium admin account you created.
