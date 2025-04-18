import sys
import time

import socket
dst_ip = sys.argv[1]
dst_port = int(sys.argv[2])
message = b"Hello from socket UDP client!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0))

print(f"Sending to {dst_ip}:{dst_port}")
sock.sendto(message, (dst_ip, dst_port))

try:
    sock.settimeout(3)
    data, addr = sock.recvfrom(1024)
    print(f"Received from {addr}: {data}")
except socket.timeout:
    print("No response received.")

sock.close()

time.sleep(5)

import subprocess
subprocess.call(["conntrack", "-L", "-p", "udp"])