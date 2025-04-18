## 1. IP (Internet Protocol)

- IP is the **core protocol of the Internet**.
- It handles **packet delivery** from source to destination across networks.
- Provides **logical addressing** via **IP addresses** (e.g., 192.168.1.1).
- IP is **connectionless and unreliable** – it doesn't guarantee delivery, order, or error-checking.

 **Key Features**:
- Routes packets across multiple networks
- Works at **Layer 3 (Network Layer)** of the OSI model
- Supports fragmentation

 **IP Header Fields (IPv4)**

| Field             | Description                                         |
|-------------------|-----------------------------------------------------|
| Version           | IP version                                          |
| IHL               | Internet Header Length (number of 32-bit words)     |
| Type of Service   | Packet priority / DSCP marking                      |
| Total Length      | Total size of the packet (header + data)            |
| Identification    | Unique ID for fragmentation                         |
| Flags             | Control bits for fragmentation (DF, MF)             |
| Fragment Offset   | Position of fragment in original packet             |
| TTL               | Time To Live (max hops before discard)              |
| Protocol          | Next layer protocol (TCP=6, UDP=17)                 |
| Header Checksum   | Checksum for error detection of the IP header       |
| Source IP         | Sender's IP address                                 |
| Destination IP    | Receiver's IP address                               |

---

## 2. UDP (User Datagram Protocol)

- UDP is a **connectionless**, **lightweight** transport protocol.
- Does **not guarantee delivery, ordering, or reliability** – but it’s faster and simpler than TCP.
- Used in real-time applications like **video streaming**, **DNS**, **VoIP**, and **games**.

 **Key Features**:
- No handshake or retransmissions
- Each packet is independent
- Low overhead and faster delivery

 **UDP Header Fields**

| Field             | Description                                        |
|-------------------|----------------------------------------------------|
| Source Port       | Port number of the sender                          |
| Destination Port  | Port number of the receiver                        |
| Length            | Length of UDP header + data                        |
| Checksum          | Error-check for header and data (optional in IPv4) |

---

## 3. TCP (Transmission Control Protocol)

- TCP is a **connection-oriented**, **reliable** protocol built on top of IP.
- Ensures **ordered**, **error-checked**, and **complete** data delivery.
- Commonly used in web traffic, email, file transfers, etc.

 **Key Features**:
- 3-way handshake (SYN, SYN-ACK, ACK) to establish connections
- Acknowledgment, retransmission, and congestion control
- Works at **Layer 4 (Transport Layer)**

**TCP Header Fields**

| Field             | Description                                        |
|-------------------|----------------------------------------------------|
| Source Port       | Port number of the sender                          |
| Destination Port  | Port number of the receiver                        |
| Sequence Number   | Byte offset of the first byte in this segment      |
| Acknowledgment No | Next expected byte from the peer (if ACK set)      |
| Data Offset       | TCP header size (in 32-bit words)                  |
| Flags             | Control bits: SYN, ACK, FIN, RST, PSH, URG         |
| Window Size       | Size of the receive window                         |
| Checksum          | Error-check for header + data                      |
| Urgent Pointer    | Indicates urgent data (rarely used)                |
| Options           | Extra settings like MSS, window scale, timestamps  |

---

## Relationship Between IP, TCP, and UDP

- **IP** handles **delivery of packets** across networks.
- **TCP and UDP** use IP to **send data between applications**.
- In packet structure:
  - IP wraps the TCP or UDP header
  - IP handles routing, while TCP/UDP handle how data is handled **at the destination**

## Congestion Algorithms – Functionalities & Capabilities 

TCP congestion control algorithms are critical for ensuring the Internet remains stable and efficient. They determine **how a sender behaves under pressure**, especially when the network is overloaded or lossy.

### Core Capabilities:
- **Bandwidth probing**: Gradually increase sending rate to test available capacity (e.g., Slow Start)
- **Loss detection**: Detect congestion via packet loss or delay (e.g., Fast Retransmit, Duplicate ACKs)
- **Backoff**: Reduce sending rate to ease pressure on the network

### Examples:
| Algorithm| Strengths                              | Weaknesses                       |
|----------|----------------------------------------|----------------------------------|
| **Reno** | Simple, works well in stable networks  | Inefficient in high-BDP networks |
| **Cubic**|  Aggressive growth, Linux default      | Bursty in some conditions        |
| **BBR**  | Measures bandwidth & RTT, proactive    | Can starve traditional flows     |

---

## TCP Errors

- **Retransmission**: The packet likely got lost or delayed. Could be congestion, routing issue, or a flaky(not working, for Pawel) link .
- **Spurious Retransmission**: Timer expired, but the original packet was actually delivered. Could indicate incorrect RTT estimation.
- **Out-of-Order**: Network took a weird path. Common in multi-path routes or asymmetric links.
- **Duplicate ACKs**: Receiver got something unexpected. Suggests packet loss or reordering.
- **Zero Window**: Receiver is overwhelmed. Flow control is throttling the sender.

---

## MTU Mismatches (we learned about MTU on previous lecture)

When two devices have different **Maximum Transmission Unit (MTU)** settings, packets may be:

1. **Fragmented** (IPv4) – inefficient, increases reassembly risk
2. **Dropped with ICMP "Fragmentation Needed"** (if DF flag is set)
3. **Lost silently** if ICMP is blocked (→ PMTU black hole)

### Path MTU Discovery (PMTUD)
- Helps avoid fragmentation by probing MTU along the route
- **Breaks** if ICMP is filtered by firewalls

---

## TCP Scans – Flags and Stealth

**XMAS and NULL scans** manipulate TCP flags to probe firewalls or OSes.

- **XMAS scan**: Sets FIN, PSH, URG → "lit up like a tree"
- **NULL scan**: No flags at all

Based on **RFC 793**, closed ports should respond with RST, while open ports **might not reply at all**.

These scans rely on **non-standard behavior** and are useful for **OS fingerprinting** and **evading intrusion detection**.

---

## Why TCP Can’t Be Used for Multicast

Multicast is inherently **one-to-many**, and TCP is designed for **one-to-one** connections. (live cast, game server)

TCP requires:
- A handshake
- Reliable state tracking
- Acknowledgments and congestion control per peer

In multicast, there's:
- No concept of "peer state"
- No way to ensure ACKs from multiple recipients

**UDP is the backbone of multicast protocols**
