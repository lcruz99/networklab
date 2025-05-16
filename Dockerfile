FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    iproute2 \
    net-tools \
    iputils-ping \
    curl \
    tcpdump \
    socat \
    iperf3 \
    iptables\
    python3-dev\
    python3-pip\
    conntrack\
    && rm -rf /var/lib/apt/lists/*

CMD ["tail", "-f", "/dev/null"]