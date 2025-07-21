#!/usr/bin/bash

/shared/common/entrypoint.sh
ip route add fd00:1::10 via fd00:3::30 dev eth0
ip route add fd00:1::20 via fd00:3::30 dev eth0

ip route add fd00:2::20 via fd00:3::30 dev eth0
ip route add fd00:2::30 via fd00:3::30 dev eth0
sleep infinity