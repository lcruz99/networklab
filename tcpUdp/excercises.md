1. Run first scapy script from client container, use tcpdump to reason about it **tcpdump -i lo udp port 8000 -n -vv**
2. Run scapy_tcp_packet.py from client container and use **tcpdump**
3. UDP connection tracking. Run udp_server.py on server and udp_contract.py on client
4. Compose server1 and client1 and run second scapy script on client use **tcpdump -i eth0 tcp port 8000 -n -vv** to see what we can see
5. Use **propper_tcp_connection** script to send tcp request from client, run **nc -l -p 8000** server on server container to see the response, use wireshark to see how the packets are behaving 

**HOMEWORK :(**
Write two scripts (sender,listener) to simulate multicast. Use pythons socket library to achieve that.

**TIPS**
apt install python3-scapy in container