
### If you're using Windows Server 2008 R2 then there is an x64 and x86 version of PowerShell both of which have to have their execution policies set. Did you set the execution policy on both hosts?

### As an Administrator, you can set the execution policy by typing this into your PowerShell window:

Set-ExecutionPolicy RemoteSigned

### For more information, see Using the Set-ExecutionPolicy Cmdlet.

Set-ExecutionPolicy Restricted

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser