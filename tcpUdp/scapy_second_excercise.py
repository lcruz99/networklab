import sys
sys.path.insert(0, '/home/saniola/.local/lib/python3.12/site-packages')

from scapy.all import IP, TCP, Raw, send, RandShort, sr1

ip = IP(dst="127.0.0.1")
tcp = TCP(sport=RandShort(), dport=8000, flags="S", seq = 123, ack = 4)
pkt = ip / tcp

response = sr1(pkt, timeout=1)
if response:
    response.show()
else:
    print("No response")