# Configuration

## Setup BGP

```sh
enable
configure terminal

# assign ASN number
router bgp <ASN>

# setting router ID (optional)
bgp router-id <ID>

# specify a neighbour router
neighbor <IP> remote-as <ASN> # for remote ASN
# if neighbour is the same ASN, it's specified as iBGP

# specify networks to advertise via BGP
network <Address> mask <Mask>

# specify default route (optional)
network 0.0.0.0
```

## Status

```sh
# list of only the best path
show ip route

# list of all possible networks learned by BGP
show ip bgp

# list of all defined neighbours and their states
show ip bgp neighbors
show ip bgp summary

# show specific neighbour details
show ip bgp neighbors <IP>
```

## Router ID

32-bit number (it looks like an  IP address,
but it's not required to be a real routable IP,
Usually the IP of the loopback interface is used, and must be unique within an AS.

An iBGP session between routers with the same BGP identifier will be rejected,
while an eBGP session is perfectly OK.

```sh
bgp router-id <ID>
```

## Loopback

Loopback interfaces are always in UP state as long as the router is running.

As long as ANY path to the router exist, the BGP session stays up,
even if other links go down.

```sh
interface Loopback0
 ip address 10.10.10.1 255.255.255.255
```

When using Loopbacks, we need to set it as the source
and enable multi-hop

```sh
router bgp 65001
 neighbor 10.10.10.2 remote-as 65002
 neighbor 10.10.10.2 update-source Loopback0 
 neighbor 10.10.10.2 ebgp-multihop 2 # enable multihop
```
