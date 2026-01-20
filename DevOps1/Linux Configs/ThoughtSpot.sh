##############################################################################
# ThoughtSpot Support Script
# Purpose: Gather information about ThoughtSpot services and cluster status
##############################################################################
#sudo tscli --adv service status tomcat
[admin@DALTSPOT01 ~]$ sudo tscli --adv service status tomcat
Service: tomcat
----------------
Status       : RUNNING
Process ID   : 13082
Uptime       : 5 days, 18 hours, 10 minutes
Port         : 8080
Log File     : /opt/thoughtspot/logs/tomcat/catalina.out
##############################################################################
# Check if Tomcat is listening on all interfaces 
[admin@DALTSPOT01 ~]$ sudo ss -tulnp | grep 8080
tcp    LISTEN     0      100    [::]:8080               [::]:*                   users:(("java",pid=13082,fd=72))
[admin@DALTSPOT01 ~]$ sudo ss -tulnp | grep 8080 | grep 0.0.0.0
##############################################################################
# Gather cluster information
###############################################################################
[admin@DALTSPOT01 ~]$ hostname
DALTSPOT01.haggarclothing.com.Haggarclothing.com
# Get the list of nodes in the cluster
[admin@DALTSPOT01 ~]$ tscli node ls
10.110.10.76
10.110.10.77
10.110.10.78
10.110.10.79
###############################################################################
# Get the cluster status
[admin@DALTSPOT01 ~]$ tscli cluster status
Cluster Status: HEALTHY
#############################################################################
# Run cluster health check
[admin@DALTSPOT01 ~]$ tscli cluster check
Connecting to hosts...
[Sun Jan 18 12:39:32 2026] START Diagnosing ssh
[Sun Jan 18 12:39:40 2026] SUCCESS
################################################################################
[admin@DALTSPOT01 ~]$ cat /etc/ntp.conf | grep server
# Use public servers from the pool.ntp.org project.
#server 0.centos.pool.ntp.org iburst
#server 1.centos.pool.ntp.org iburst
#server 2.centos.pool.ntp.org iburst
#server 3.centos.pool.ntp.org iburst
#broadcast 192.168.1.255 autokey        # broadcast server
#broadcast 224.0.1.1 autokey            # multicast server
#manycastserver 239.255.254.254         # manycast server
server 10.110.10.100
#############################################################################
# Check NTP service status  and restart if needed
[admin@DALTSPOT01 ~]$ systemctl status ntpd
● ntpd.service - Network Time Service
   Loaded: loaded (/usr/lib/systemd/system/ntpd.service; enabled; vendor preset: disabled)
   Active: active (running) since Tue 2024-08-06 19:31:18 CDT; 1 years 5 months ago
 Main PID: 4304 (ntpd)
   CGroup: /system.slice/ntpd.service
           └─4304 /usr/sbin/ntpd -u ntp:ntp -g

Jan 17 14:29:01 DALTSPOT01.haggarclothing.com.Haggarclothing.com ntpd[4304]: Listen normally on 12 eth2 10.110.10.76 UDP 123
Jan 17 14:29:01 DALTSPOT01.haggarclothing.com.Haggarclothing.com ntpd[4304]: new interface(s) found: waking up resolver
Jan 17 14:29:03 DALTSPOT01.haggarclothing.com.Haggarclothing.com ntpd[4304]: Listen normally on 13 eth2 fe80::ae1f:6bff:fe8d:fb54 UDP 123
Jan 17 14:29:03 DALTSPOT01.haggarclothing.com.Haggarclothing.com ntpd[4304]: new interface(s) found: waking up resolver
Jan 17 19:01:54 DALTSPOT01.haggarclothing.com.Haggarclothing.com ntpd[4304]: Deleting interface #13 eth2, fe80::ae1f:6bff:fe8d:fb54#123, interface stats: re...1 secs
Jan 17 19:01:54 DALTSPOT01.haggarclothing.com.Haggarclothing.com ntpd[4304]: Deleting interface #12 eth2, 10.110.10.76#123, interface stats: received=192, s...3 secs
Jan 17 19:01:54 DALTSPOT01.haggarclothing.com.Haggarclothing.com ntpd[4304]: 10.110.10.100 interface 10.110.10.76 -> (none)
Jan 17 19:04:55 DALTSPOT01.haggarclothing.com.Haggarclothing.com ntpd[4304]: Listen normally on 14 eth2 10.110.10.76 UDP 123
Jan 17 19:04:55 DALTSPOT01.haggarclothing.com.Haggarclothing.com ntpd[4304]: Listen normally on 15 eth2 fe80::ae1f:6bff:fe8d:fb54 UDP 123
Jan 17 19:04:55 DALTSPOT01.haggarclothing.com.Haggarclothing.com ntpd[4304]: new interface(s) found: waking up resolver
Hint: Some lines were ellipsized, use -l to show in full.
[admin@DALTSPOT01 ~]$ sudo systemctl restart ntpd
#############################################################################
# Manually sync time with NTP server and check configuration  
[admin@DALTSPOT01 ~]$ sudo ntpdate -d 10.110.10.111
18 Jan 13:04:30 ntpdate[11728]: ntpdate 4.2.6p5@1.2349-o Tue Jun 23 15:38:19 UTC 2020 (1)
Looking for host 10.110.10.111 and service ntp
host found : DALDC10.haggarclothing.com
transmit(10.110.10.111)
receive(10.110.10.111)
transmit(10.110.10.111)
receive(10.110.10.111)
transmit(10.110.10.111)
receive(10.110.10.111)
transmit(10.110.10.111)
receive(10.110.10.111)
server 10.110.10.111, port 123
stratum 3, precision -23, leap 00, trust 000
refid [10.110.10.111], delay 0.02586, dispersion 0.00000
transmitted 4, in filter 4
reference time:    ed17aa49.3cbead4f  Sun, Jan 18 2026 12:51:53.237
originate timestamp: ed17ad44.44ae60d0  Sun, Jan 18 2026 13:04:36.268
transmit timestamp:  ed17ad44.44961f51  Sun, Jan 18 2026 13:04:36.267
filter delay:  0.02588  0.02588  0.02588  0.02586
         0.00000  0.00000  0.00000  0.00000
filter offset: 0.000267 0.000241 0.000243 0.000237
         0.000000 0.000000 0.000000 0.000000
delay 0.02586, dispersion 0.00000
offset 0.000237
###########################################################################
# Check DNS configuration
[admin@DALTSPOT01 ~]$ cat /etc/resolv.conf
# Generated by NetworkManager
search haggarclothing.com.Haggarclothing.com Haggarclothing.com
nameserver
[admin@DALTSPOT01 ~]$ sudo vi /etc/ntp.conf
systemctl status ntpd
systemctl status chronyd
sudo systemctl restart ntpd
### NTP Commands
grep server /etc/ntp.conf
ntpq -p
ntpdate -u 10.110.10.111
### NTP Commands to run
##############################################################################
sudo ntpdate -u 10.110.10.111
sudo systemctl restart ntpd
ntpq -p
### DNS Commands to run
##################################################################
cat /etc/resolv.conf
sudo vi /etc/resolv.conf
sudo ss -tulnp | grep 8080
sudo tscli service status
## Summary of commands to run
##################################################################
tscli node ls
tscli cluster status
tscli cluster check
tscli --adv service status tomcat
#Restart thoughspot services dataflow and etl_http_server
##################################################################
tscli --adv service restart dataflow
tscli --adv service restart etl_http_server
###################################################################
