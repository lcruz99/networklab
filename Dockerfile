FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    iproute2 \
    net-tools \
    iputils-ping \
    curl \
    tcpdump \
    socat \
    iperf3 \
    iptables \
    python3 \
    python3-requests \
    tree \
    vim \
    iputils-arping \
    arp-scan \
    frr \
    traceroute \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

CMD ["tail", "-f", "/dev/null"]

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y frr frr-pythontools iproute2 iputils-ping tcpdump nano && \
    rm -rf /var/lib/apt/lists/*

# Turn on IP forwarding by default
RUN echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf && \
    echo "net.ipv4.conf.all.rp_filter=0" >> /etc/sysctl.conf && \
    echo "net.ipv4.conf.default.rp_filter=0" >> /etc/sysctl.conf

# Enable zebra + ripd
RUN sed -i 's/zebra=no/zebra=yes/' /etc/frr/daemons && \
    sed -i 's/ripd=no/ripd=yes/' /etc/frr/daemons && \
    sed -i 's/vtysh_enable=no/vtysh_enable=yes/' /etc/frr/daemons

# Start FRR in foreground (so container keeps running)
CMD sysctl -p && /usr/lib/frr/frrinit.sh start && tail -f /var/log/frr/frr.log || tail -f /dev/null