#!/usr/bin/bash
/shared/common/entrypoint.sh
ip route add fd00:1::10 via fd00:2::20 dev eth0
ip route add fd00:1::20 via fd00:2::20 dev eth0
sleep infinity