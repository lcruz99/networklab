# Network Address Translation (NAT)

## What is NAT?

**NAT (Network Address Translation)** is a method used by routers to translate private IP addresses to a public IP address — and vice versa — allowing multiple devices to share a single public IP.

### Why is NAT used?

- Solves IPv4 address exhaustion
- Provides basic firewalling by hiding internal IPs

---

## How NAT Works

When a device behind a NAT sends a packet to the Internet:

1. The NAT router **replaces the source IP and port** with its own.
2. The router records this translation in the **NAT table**.
3. When the response arrives, the router **uses the NAT table** to translate it back to the internal address.

### Example:

```
192.168.0.10:12345 → NAT → 203.0.113.5:45000
```

When a reply comes back to `203.0.113.5:45000`, the NAT router knows it should go to `192.168.0.10:12345`.

---

## NAT Table

The NAT table keeps track of translated connections.

| Protocol | Internal IP\:Port  | External IP\:Port | State       |
| -------- | ------------------ | ----------------- | ----------- |
| UDP      | 192.168.0.10:12345 | 203.0.113.5:45000 | ESTABLISHED |
| TCP      | 192.168.0.11:54321 | 203.0.113.5:45100 | ESTABLISHED |


## Types of NAT

### 1. Static NAT

- One-to-one mapping between internal and external IPs
- Used for hosting services behind NAT

### 2. Dynamic NAT

- Internal IPs are mapped to a **pool** of external IPs
- Mapping changes depending on availability

### 3. PAT (Port Address Translation), aka NAT Overload

- Most common
- All internal devices share a **single public IP**
- Each connection is identified by a unique port

---

## NAT Behavior Types (Used in P2P)

| Type                | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **Full Cone**       | Any external host can send to the mapped IP and port         |
| **Restricted Cone** | Only IPs previously contacted can send replies               |
| **Port Restricted** | Only IP\:port pairs previously contacted can reply           |
| **Symmetric**       | Each destination gets a unique mapping — hardest to traverse |

These types affect protocols like VoIP, multiplayer games, and NAT hole punching.

## Summary

- NAT rewrites IPs and ports to allow many devices to share one public IP
- A **NAT table** keeps track of connection mappings
- Most common NAT is **PAT (Port Address Translation)**
- NAT behavior types impact P2P connectivity
- Use `iptables` and `conntrack` to configure and inspect NAT

NAT is fundamental to IPv4 networking and affects routing, firewalls, and peer communication.

