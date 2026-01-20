1. Script to Pull Users from a Server (Local Users or Domain Users)
This script pulls all local users from a specific server. If you're querying a domain controller or want domain users, let me know.

# Script 1: Get Local Users on a Remote Server
$serverName = "YourServerName"

Invoke-Command -ComputerName $serverName -ScriptBlock {
    Get-LocalUser | Select-Object Name, Enabled, LastLogon
}
🔐 Make sure PowerShell Remoting is enabled (Enable-PSRemoting) on the target server.
2. Script to Get Last Login Time for Users on That Server
This uses event logs to track the last login for each user.

# Script 2: Get Last Login Time of Users
$serverName = "YourServerName"

Invoke-Command -ComputerName $serverName -ScriptBlock {
    $logins = Get-WinEvent -LogName Security -FilterHashtable @{Id=4624} -MaxEvents 1000 |
              Where-Object { $_.Properties[5].Value -ne "ANONYMOUS LOGON" } |
              Select-Object @{Name="UserName";Expression={ $_.Properties[5].Value }},
                            @{Name="TimeCreated";Expression={ $_.TimeCreated }}

    $logins | Group-Object UserName | ForEach-Object {
        $_.Group | Sort-Object TimeCreated -Descending | Select-Object -First 1
    }
}
⚠️ Event ID 4624 indicates successful logons. This approach may miss logons if the event log is trimmed or auditing is disabled.
3. Script to Pull General Event Logs (e.g., Application, System, Security)
# Script 3: Get Event Logs (example: System log)
$serverName = "YourServerName"
$logName = "System"  # Change to Application or Security if needed

Invoke-Command -ComputerName $serverName -ScriptBlock {
    Get-EventLog -LogName $using:logName -Newest 50 | Select-Object TimeGenerated, EntryType, Source, Message
}
Would you like all of these scripts combined into a single tool or run as separate modules? And are you working in an AD environment or on standalone servers?

You said:
best powershelgl scripts for systems engineers
ChatGPT said:
Nice — you're looking for some solid PowerShell tools for Systems Engineers. Here’s a curated list of top PowerShell scripts that are highly useful for day-to-day sysadmin/system engineering tasks, whether you're managing AD, servers, event logs, or patching. These can be modularized or put into a single toolkit.

🔧 1. Get System Info (RAM, CPU, OS, etc.)
# Get basic system info
Get-ComputerInfo | Select-Object CsName, OsName, OsVersion, WindowsProductName, OsArchitecture, CsProcessors, CsTotalPhysicalMemory
🔍 2. List Installed Applications
# List installed applications (32-bit and 64-bit)
Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*, `
                 HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* |
    Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Sort-Object DisplayName
🧑‍💻 3. Get Logged-In User(s) on a Remote Machine
# Check who is logged into a machine
Invoke-Command -ComputerName "YourServerName" -ScriptBlock {
    query user
}
📦 4. Check for Pending Reboot (Patching Readiness)
# Check if reboot is pending
$PendingReboot = @()
$Computers = @("Server1", "Server2")  # Add your servers here

foreach ($Computer in $Computers) {
    $RebootRequired = Invoke-Command -ComputerName $Computer -ScriptBlock {
        Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending"
    }
    $PendingReboot += [PSCustomObject]@{
        Computer = $Computer
        RebootPending = $RebootRequired
    }
}

$PendingReboot
🧾 5. Export Event Logs to CSV
# Export system logs to CSV
Get-WinEvent -LogName System -MaxEvents 100 | 
    Select-Object TimeCreated, Id, LevelDisplayName, Message | 
    Export-Csv "C:\Logs\SystemLogs.csv" -NoTypeInformation
🔐 6. Active Directory - Get Locked Out Users
# Show all locked-out AD users
Search-ADAccount -LockedOut | Select-Object Name, SamAccountName, LockedOut
Requires RSAT or ActiveDirectory module.
📡 7. Test Network Connectivity (Ping sweep)
# Quick ping sweep
1..254 | ForEach-Object {
    $ip = "192.168.1.$_"
    if (Test-Connection -ComputerName $ip -Count 1 -Quiet) {
        Write-Host "$ip is online"
    }
}
📁 8. Search for Large Files (Disk Cleanup Support)
# Find large files over 1GB
Get-ChildItem -Path "C:\" -Recurse -ErrorAction SilentlyContinue |
    Where-Object { $_.Length -gt 1GB } |
    Select-Object FullName, @{Name="SizeGB";Expression={[math]::Round($_.Length / 1GB, 2)}}
📤 9. Remote Software Deployment via Chocolatey
# Install software on remote computer via Chocolatey
Invoke-Command -ComputerName "YourServerName" -ScriptBlock {
    choco install googlechrome -y
}
🔁 10. Restart Multiple Remote Computers
# Restart servers
$computers = @("Server1", "Server2")
foreach ($comp in $computers) {
    Restart-Computer -ComputerName $comp -Force
}
Let me know if you want to bundle these into a GUI tool or create a modular script runner. Also happy to tailor this list for cloud/hybrid environments, security-focused ops, or automated patching.

You said:
I need more 
ChatGPT said:
Memory Updated
Absolutely — here’s a more advanced batch of PowerShell scripts perfect for Systems Engineers handling infrastructure, security, automation, and monitoring.

🛡️ 11. Check if Windows Defender is Enabled & Running

# Check Windows Defender status
Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled
🗃️ 12. Audit Local Admin Group Membership on Multiple Machines

# Audit local admins
$computers = @("Server1", "Server2")

foreach ($comp in $computers) {
    Invoke-Command -ComputerName $comp -ScriptBlock {
        Get-LocalGroupMember -Group "Administrators" | Select-Object Name, ObjectClass
    } | Format-Table -Property Name, ObjectClass -AutoSize -Wrap
}
💼 13. Create Local User and Add to Group

# Create a local user and add to Administrators group
$Username = "SysOpsUser"
$Password = Read-Host -AsSecureString "Enter Password"

New-LocalUser -Name $Username -Password $Password -FullName "SysOps Local Admin" -Description "For system maintenance"
Add-LocalGroupMember -Group "Administrators" -Member $Username
🔄 14. Scheduled Task Creation

# Create a scheduled task that runs PowerShell script every day at 6 PM
$Action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-File C:\Scripts\Task.ps1"
$Trigger = New-ScheduledTaskTrigger -Daily -At 6pm
Register-ScheduledTask -Action $Action -Trigger $Trigger -TaskName "DailyTask" -Description "Daily Script Run"
🔍 15. Monitor a Service and Restart if Stopped

# Monitor and restart if service is down
$serviceName = "Spooler"
$server = "ServerName"

Invoke-Command -ComputerName $server -ScriptBlock {
    $svc = Get-Service -Name $using:serviceName
    if ($svc.Status -ne "Running") {
        Restart-Service -Name $using:serviceName
        Write-Output "$using:serviceName restarted on $env:COMPUTERNAME"
    } else {
        Write-Output "$using:serviceName is running fine."
    }
}
🧠 16. Get Memory & CPU Usage of Remote Machine

# Get CPU and RAM usage from remote server
$server = "ServerName"
Invoke-Command -ComputerName $server -ScriptBlock {
    Get-CimInstance Win32_OperatingSystem | Select-Object @{Name="FreeMemory(GB)";Expression={[math]::Round($_.FreePhysicalMemory / 1MB, 2)}},
                                                        @{Name="TotalMemory(GB)";Expression={[math]::Round($_.TotalVisibleMemorySize / 1MB, 2)}}

    Get-CimInstance Win32_Processor | Select-Object Name, LoadPercentage
}
📜 17. Search Event Logs for Specific Error Codes

# Look for specific error codes in System logs
Get-WinEvent -FilterHashtable @{LogName='System'; ID=10016} -MaxEvents 100 |
    Select-Object TimeCreated, Id, LevelDisplayName, Message
🧭 18. List Network Adapters and IP Config

# Show adapter settings
Get-NetAdapter | Select Name, Status, MacAddress, LinkSpeed
Get-NetIPAddress | Where-Object {$_.AddressFamily -eq "IPv4"} | Select IPAddress, InterfaceAlias
🧱 19. Check Disk Space on Remote Machines

# Check free space
$computers = @("Server1", "Server2")
foreach ($comp in $computers) {
    Invoke-Command -ComputerName $comp -ScriptBlock {
        Get-PSDrive -PSProvider FileSystem | Select-Object Name, @{n="Free(GB)";e={[math]::Round($_.Free/1GB,2)}}, @{n="Used(GB)";e={[math]::Round(($_.Used)/1GB,2)}}
    }
}
🔄 20. Copy File to Multiple Machines and Log the Result

# Copy file to multiple machines
$computers = @("Server1", "Server2")
$file = "C:\Deploy\update.bat"
$dest = "C$\Temp\update.bat"

foreach ($comp in $computers) {
    try {
        Copy-Item -Path $file -Destination "\\$comp\$dest" -Force
        Write-Output "$comp - File copied successfully"
    } catch {
        Write-Output "$comp - ERROR: $($_.Exception.Message)"
    }
}
🔧 Want these scripts bundled into a GUI, menu-based toolkit, or module?
I can help you package these into:

A PowerShell GUI tool (WPF or WinForms)
A menu-driven script (like an all-in-one sysadmin launcher)
A PS module for import and reuse
Want that? And what OS/domain environment are you mainly working with — hybrid, on-prem, Azure AD, etc.?