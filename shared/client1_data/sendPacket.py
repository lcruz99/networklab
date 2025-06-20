import sys
sys.path.insert(0, '/home/saniola/.local/lib/python3.12/site-packages')

### run 'apt install python3-scapy' on container that runs this script
from scapy.all import IP, TCP, Raw, send, RandShort, sr1, sniff, UDP

pkt = IP(dst="172.22.0.5") / UDP(sport=12345, dport=54321) / Raw(load="hello")
send(pkt, iface="eth0")