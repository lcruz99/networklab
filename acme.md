# Routing
1. ip r
2. ip r del default
3. ip r add default via <host_ip>

# tcpdump icmp

# natting  

### 1
iptables -t nat -A POSTROUTING -o eth1 -j MASQUERADE

**Enables dynamic SNAT (source NAT), allowing internal clients to access external networks (like the internet) using the router’s IP on eth1.**

### 2
iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT

**Accepts all packets going from eth0 to eth1 regardless of connection state**

### 3
iptables -A FORWARD -i eth0 -o eth1 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT

**Accepts return traffic (e.g. replies to already-established connections) going from eth0 to eth1 and uses conntrack to track connection state**

### 4
iptables -A FORWARD -j DROP

**Drops all other traffic not matched by earlier rules**

### 5
iptables -A FORWARD -m conntrack --ctstate NEW -j DROP

**Drops all new connection attempts, regardless of interface**

### 6
iptables -t nat -L -n -v --line-numbers

**list all NAT table rules with line numbers:**

### 7

apt update && apt install conntrack -y

conntrack -F
conntrack -L

### 8

nice depiction of packet route
https://en.wikipedia.org/wiki/Iptables#/media/File:Netfilter-packet-flow.svg