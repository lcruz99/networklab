import sys
sys.path.insert(0, '/home/saniola/.local/lib/python3.12/site-packages')

from scapy.all import IP, TCP, Raw, send, RandShort, sr1

ip = sys.argv[1]
dst_port = int(sys.argv[2])

ip = IP(dst=ip)
src_port = RandShort()
tcp = TCP(sport=src_port, dport=dst_port, flags="S", seq = 123, ack = 4)
pkt = ip / tcp

syn_ack  = sr1(pkt, timeout=1) #sending a syn request

print("ACK")
syn_ack.show()

if not syn_ack :
    print("no ack!! :()")
    exit()

ack = TCP(sport=src_port, dport=dst_port, flags="A",
          seq=syn_ack.ack, ack=syn_ack.seq + 1)
send(ip/ack)

#connection has been established lets send some data
data = TCP(sport=src_port, dport=dst_port, flags="PA",
           seq=ack.seq, ack=ack.ack) / "Hello from Scapy!"
send(ip/data)