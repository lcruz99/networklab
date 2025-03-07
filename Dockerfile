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
    && rm -rf /var/lib/apt/lists/*

CMD ["tail", "-f", "/dev/null"]