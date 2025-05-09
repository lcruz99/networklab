import sys
sys.path.insert(0, '/home/saniola/.local/lib/python3.12/site-packages')

from scapy.all import IP, UDP, Raw, send, RandShort
# Build a simple UDP packet
packet = IP(dst="172.20.0.3") / UDP(dport=8000, sport=RandShort()) / Raw(load="Hello from Scapy!")

# Send the packet
send(packet)

print("UDP packet sent to localhost:8000")
