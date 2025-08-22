#!/bin/sh
set -e

# sysctls
sysctl -w net.ipv4.ip_forward=1
sysctl -w net.ipv4.conf.all.rp_filter=0
sysctl -w net.ipv4.conf.default.rp_filter=0

# start FRR
/usr/lib/frr/frrinit.sh start

# keep container alive
exec tail -f /var/log/frr/frr.log