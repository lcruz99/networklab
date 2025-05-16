# Firewall


A firewall is a system that controls incoming and outgoing network traffic based on predetermined security rules.

## Netfilter  framework
- Packet filtering / Hooks
- Conntrack
- NAT
- Userspace libraries
- iptables/nftables

### Conntrack module
- Is part of the kernel that is responsible for tracking connections 
- There is also a userspace tool conntrack to interact with kernel component

### NAT module
- Is part of the kernel responsible for applying NAT transformations to the packets

### Userspace libraries
- Netfilter allows userspace async packet handling

### Iptables
- Iptables (ip6tables, arptables, ebtables) are still legacy but widely used
- Userspace tools used to configure firewall/nat rules
- Rules are stored and executed in chains which are hooked into the netfilter hooks.
- Chains of the same type/use case are stored together inside 5 predefined tables: filter, nat, raw, mangle, security.
---
- filter: default table. Rules from this table should be responsible for filtering the packets that is either accepting or dropping.
- nat: rules from this table are special. Only first packet from the connection is sent to them. They are responsible only for configuring NAT and later conntrack and nat framework handle the natting for the rest of the packets.
- mangle: rules from this table should be used for mangling the packets.
- raw: rules from this table have the highest priority. Even higher then conntrack. They are actually only base hooks called before conntrack and their main purpose is to mark packets with NOTRACK target to disable connection tracking.
- security: for Mandatory Access Control (MAC) networking rules in SELinux
---


### Nftables
- Is the new improved version of iptables
- faster and more flexible


### Rule example
Drop all tcp packets coming from 172.23.0.2 (client 1)
- iptables -A INPUT -p tcp -s 172.23.0.2 -j DROP
- nft add rule ip filter INPUT ip protocol tcp ip saddr 172.23.0.2 counter drop

### Links
[Netfilter official)](https://www.netfilter.org/)
