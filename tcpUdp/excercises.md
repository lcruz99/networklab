1. Run wireshark and Check how a TCP and UDP packet looks
2. Run first scapy script, use tcpdump to reason about it **tcpdump -i lo tcp port 8000 -n -vv**
3. Compose server1 and client1 and run second scapy script on client use **tcpdump -i eth0 tcp port 8000 -n -vv** to see what we can see
4. Use **propper_tcp_connection** script to send tcp request from client, run **nc -l -p 8000** server on server container to see the response, use wireshark to see how the packets are going 