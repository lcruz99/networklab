import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 8000))  # Bind to all interfaces, port 8000

print("UDP server listening on port 8000...")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received from {addr}: {data.decode(errors='ignore')}")

    # Echo reply to source
    reply = b"Pong from UDP server!"
    sock.sendto(reply, addr)
    print(f"Sent reply to {addr}")