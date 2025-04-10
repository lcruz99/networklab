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
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

CMD ["tail", "-f", "/dev/null"]