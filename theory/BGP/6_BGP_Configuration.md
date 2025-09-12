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
