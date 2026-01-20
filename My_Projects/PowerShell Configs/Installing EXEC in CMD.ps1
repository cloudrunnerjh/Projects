msiexec /i "\\tribaldc1\tierpoint\check_mk_agent.msi" /qn WIXUI_CLEANINSTALL=
netsh advfirewall firewall add rule name="Checkmk Agent" description="Inbound to Checkmk Agent" dir=in localport=6556 protocol=tcp action=allow program="C:\ProgramData\checkmk\agent\bin\cmk-agent-ctl.exe" profile=domain,private,public enable=yes
netsh advfirewall firewall add rule name="Checkmk Ping" description="For Checkmk Monitoring Service" dir=in protocol=icmpv4 action=allow  profile=domain,private,public enable=yes program=System


CS2274244 - No longer receiving a reply from Fed Ex on HDEV.
Hello TP,

Could you verify if we have Fedex policy implemented that will allow traffic coming in out from 10.42.0.100 (HDEV) to 10.110.18.43 (FedEx server) and From (10.110.18.43) back to (10.42.0.100)?

Below are the 2 IP’s that I send/receive data from. Port 2000 on the Fed Ex Server

HDEV IP: 10.110.18.43 (Destination)
Fed Ex Server: 10.42.0.100 (Source)
Server Name: FTWFDX05
Port: 2000
Preferred contact method: jonathan.hernandez@randa.net