# Dynamic Routing Protocols: RIP vs OSPF

---

## 1. Introduction

- **Dynamic routing protocols** allow routers to automatically exchange routes.
- They adapt to topology changes without manual configuration.
- Two classic IGPs (Interior Gateway Protocols):
  - **RIP (Routing Information Protocol)** → simple, distance-vector.
  - **OSPF (Open Shortest Path First)** → advanced, link-state.

---

## 2. RIP (Routing Information Protocol)

### Basics
- Type: **Distance-Vector Protocol**
- Algorithm: **Bellman–Ford**
- Transport: **UDP, port 520**
- Metric: **Hop count**
  - Max hops: **15**
  - 16 = Infinity (unreachable)

### Operation
- Routers send **entire routing table** every **30 seconds**.
- Updates sent to **224.0.0.9 (multicast)** in RIPv2.
- Status check = **timeout**:
  - 180s → route marked invalid
  - 240s → route removed

### Advantages
- Very simple to configure.
- Low resource usage.
- Works in small, flat networks.

### Disadvantages
- Slow convergence.
- Hop limit restricts network size.
- Prone to loops (needs split-horizon, poisoned reverse).

---

## 3. OSPF (Open Shortest Path First)

### Basics
- Type: **Link-State Protocol**
- Algorithm: **Dijkstra (SPF)**
- Transport: **IP, protocol 89** (not TCP/UDP)
- Metric: **Cost** (based on bandwidth, configurable)

### Operation
- Routers exchange **Hello packets** to form neighbor relationships.
- Build a **Link State Database (LSDB)** with full topology.
- Run SPF to compute shortest paths.
- Flood incremental updates only when topology changes.
- Hierarchical design:
  - **Areas** (Area 0 = backbone).

### Advantages
- Fast convergence.
- Scales well (hierarchical).
- More efficient and loop-free.
- Supports VLSM, authentication, route summarization.

### Disadvantages
- More complex to configure.
- Higher memory and CPU usage.
- Requires consistent design (areas, timers).

---

## 4. Key Differences

| Feature              | RIP                       | OSPF                        |
|----------------------|---------------------------|-----------------------------|
| Protocol type        | Distance-vector           | Link-state                  |
| Algorithm            | Bellman–Ford              | Dijkstra (SPF)              |
| Transport            | UDP/520                   | IP protocol 89              |
| Metric               | Hop count (max 15)        | Cost (bandwidth-based)      |
| Updates              | Periodic (every 30s)      | Triggered, incremental      |
| Convergence speed    | Slow                      | Fast                        |
| Scalability          | Small networks only       | Large, hierarchical         |
| Loop prevention      | Split-horizon, poison rev | Built-in SPF/LSDB           |

---

### Implementation details

### What is FRR?

FRR (Free Range Routing) is an open-source routing software suite.
It’s used to implement routing protocols (RIP, OSPF, BGP, IS-IS, etc.) in Linux.

It runs as user-space daemons (background processes).

It talks to the Linux kernel routing table through the zebra daemon.

You interact with it using vtysh (CLI), which connects to those daemons.

### What is Zebra?

zebra is the core daemon.

It manages the RIB (Routing Information Base), the "brain" that decides which routes go into the Linux kernel routing table.

Other protocol daemons (ripd, ospfd, bgpd, etc.) send routes to zebra.

Zebra installs the best routes into the Linux kernel via netlink.

Think of zebra as the traffic controller between protocols and the kernel.

### TLDR;

FRR = suite of daemons for routing.

zebra = central brain that talks to the kernel.

Protocol daemons = implement specific routing protocols.

daemons file = enable/disable which daemons run.

frr.conf = actual routing configuration.

watchfrr = keeps everything alive.