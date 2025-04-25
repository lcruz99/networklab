# Windows workshop

Windows is a closed source OS developed by Microsoft and based on NT Kernel.

We have the already known tools available on other OSs like: wireshark, ping, tracert, nslookup, arp, netstat

## Core windows neworking tools

### ipconfig - CLI
>  ipconfig /all
>  ipconfig /release   -> **Tells Windows to drop (release) its current IP address** from the network.
>  ipconfig /renew    -> **Requests a new IP address** from the DHCP server.
>  ipconfig /flushdns -> Flush DNS

### netsh - CLI - Network configuration and diagnostics
> netsh interface ipv4 show config ->  List all interfaces and IP addresses:
> netsh interface ip show config name="Ethernet"  -> Show IP settings for a specific interface
> netsh interface ip set dns name="Ethernet" static 8.8.8.8 -> Set a custom DNS

### powershell - CLI - mostly used for scripting
Has multiple commands for networking stuff
> Get-NetIPConfiguration -> shows IP/DNS/Gateways similar to ipconfig
> Set-NetIPAddress -> Set static IP similar with **netsh interface ip**
> Set-DnsClientServerAddress -> Set DNS similar with **netsh interface ip set dns**
> Get-NetAdapter -> List network adapters similar with **netsh interface show**
> Enable/Disable-NetAdapter -> Turn adapters on/off
> Get-NetRoute -> View routing table
> New-NetRoute/Remove-NetRoute -> Add/remove route
> Test-NetConnection -> Ping, port check and traceroute in one Ex: **Test-NetConnection google.com -Port 443**
> Resolve-DnsName -> DNS lookup
> New-NetFirewallRule -> Add a firewall rule Ex: **New-NetFirewallRule -DisplayName "AllowPort8080" -Direction Inbound -LocalPort 8080 -Protocol TCP -Action Allow**
> Get-NetFirewallRule -> View rules
> Remove-NetFirewallRule -> Delete rules

### Network and Sharing Center - GUI 
See and manage active networks

### Device Manager -> Network Adapters - GUI
Check driver, disable/enable adapters

### Windows Firewall with Advanced Security - GUI
Configure inbound/inbound rules

### Event viewer - GUI 
Logs DNS, DHCP client events and more

### Resource Monitor - GUI
Bandwidth monitor 


## SysInternals tools
SysInternals is a collection of powerfull tools for windows.

### TCPView - GUI
A real-time utility that shows a detailed list of all **open TCP and UDP connections** on your system, along with the process that owns each connection.

### PsPing - CLI
PsPing is a **network performance tool** that goes beyond simple `ping`. It measures network **latency, bandwidth, and packet loss** for TCP and UDP connections.

### ProcMon - GUI
**ProcMon** isn't a networking tool by design, but it’s extremely useful for **monitoring network activity** on your system by logging **file system** and **registry operations**, along with **network activity** initiated by processes.


## Other tools
## Hercules - GUI
A free tool for debugging and testing serial (RS232) communication and network (TCP/UDP) protocols.
