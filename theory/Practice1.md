## Practice 1 - Sniffing packets

-`export SSLKEYLOGFILE=~/sslkeys.log`
- openssl req -x509 -newkey rsa:2048 -keyout private.key -out public.crt -days 365 -nodes
- dd if=/dev/zero of=zero_file bs=1M count=100
- curl -X http://172.20.0.3:8000/api?user=luis&password=123456
- tc qdisc add dev eth0 root tbf rate 100kbps burst 32kbit latency 400ms
- tc qdisc add dev eth0 root netem delay 50ms reorder 25% 50%
- tc qdisc add dev eth0 root netem loss 20%