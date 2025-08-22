# Routing
1. ip r
2. ip r del default
3. ip r add default via <host_ip>

# tcpdump icmp

# show route
vtysh -c "show ip route"

# restart on client2 and server2
/usr/lib/frr/frrinit.sh restart

# check zebra
pgrep -a zebra

# kernel routing table
ip route show