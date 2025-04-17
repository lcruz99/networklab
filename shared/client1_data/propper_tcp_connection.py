import socket
import sys 

ip = sys.argv[1]
port = int(sys.argv[2])

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Connecting to {ip}:{port}...")
    s.connect((ip, port))
    
    print("Connected! Sending message...")
    s.sendall(b"Hello from Python socket!\n")

    # Receive response
    data = s.recv(1024)
    print(f"[<] Received: {data.decode()}")