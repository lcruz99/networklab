# Current topology

```
+------------+         +------------+         +------------+         +------------+
|  Client1   |---------|  Server1   |---------|  Server2   |---------|  Client2   |
| fd00:1::10 |         | fd00:1::20 |         | fd00:2::30 |         | fd00:3::40 |
|            |         | fd00:2::20 |         | fd00:3::30 |         |            |
+------------+         +------------+         +------------+         +------------+

```

# IPv6

Internet protocol version 6 was developed because its predecesor IPv4 was running out of unique IP addresses.
It is desined with 128 bits/16 bytes for address. Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7734

Key updates/features:

- Larger address space
- Simple header, it removes the checksum and it's easier and faster to route
- It has built-in security. IPSec si mandatory in IPv6.
- Technically it removes the need of NAT

How addresses can look:

- 2001:0db8:85a3:0000:0000:8a2e:0370:7334
- 2001:0db8:85a3::8a2e:0370:7334
- 2001:db8:85a3::8a2e:370:7334

---
# IPv6 Features

```
    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |Version| Traffic Class |         **Flow Label**                |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |         Payload Length        |  Next Header  |   Hop Limit   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                                                               |
   +                                                               +
   |                                                               |
   +                         Source Address                        +
   |                                                               |
   +                                                               +
   |                                                               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                                                               |
   +                                                               +
   |                                                               |
   +                      Destination Address                      +
   |                                                               |
   +                                                               +
   |                                                               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

## Flow label - [RFC](https://www.rfc-editor.org/rfc/rfc6437)

Flow label is a 20-bit field in the IPv6 header and it can be used to label a flow to be specially handled by routers: Ex. low latency, consistent path etc

A flow is a sequence of packets sent from a source to a destination that require the same handling by the routers.

The sad reality is that it is not really used. Most routers ignore it and most operating systems don't use it by default, they just set it to 0 or to some default.

Exercise 1

We can see the flow labels using tcpdump in verbose mode:

```
// Start a tcpdump on the server1
tcpdump -nv icmp6 and icmp6[0] == 128

// Ping client2 from client1
ping6 -c 1 fd00:3::40
ping6 -c 1 fd00:3::40 -F 0x12345
```

### Traffic control

We can use `tc` traffic control command to control how flows with different labels behave.

Terminology:

- A **class** in the context of `tc` refers to a category that holds a set of rules and parameters for managing a specific subset of network traffic.
- A **filter** in the context of `tc` is applied to classify packets based on specific criteria and direct them to the appropriate class, allowing more granular control.
- **qdisc** (queueing discipline). Whenever the kernel needs to send a packet to an interface it is enqueued to the qdisc configured for that interface. Immediately afterwards, the kernel tries to get as many packets as possible from the qdisc for giving them to the network adapter.
- **HTB** stands for Hierarchical Token Bucket algorithm. It can be conceptually understood as follows:
    - A token is added to the bucket every 1/r seconds. 
    - The bucket can hold at the most b tokens. If a token arrives when the bucket is full, it is discarded.
    - When a packet of n bytes arrives,
        - if at least n tokens are in the bucket, n tokens are removed from the bucket, and the packet is sent to the network.
        - if fewer than n tokens are available, no tokens are removed from the bucket, and the packet is considered to be non-conformant.

To set 100Mbits/s limit for 0x12345 flow label and 200Mbits/s for 0x54321 we should:
1. `tc qdisc add dev eth1 root handle 1: htb default 12` - Adds an HTB qdisc to the root of the `eth1` interface, specifying a default class (1:12) for unmatched traffic.
2. `tc class add dev eth1 parent 1: classid 1:1 htb rate 100Mbit quantum 1500` - Adds a class (1:1) to the HTB qdisc with a rate limit of 100Mbps
3. `tc class add dev eth1 parent 1: classid 1:2 htb rate 200Mbit quantum 1500` - Adds a class (1:2) to the HTB disk with a rate limit of 200Mbps
4. `tc filter add dev eth1 parent 1: protocol ipv6 u32 match ip6 flowlabel 0x12345 0xFFFFF flowid 1:1` - Attaches a filter to the root qdisc, directing traffic with flow label 0x12345 to the class with a rate of 100Mbps
5. `tc filter add dev eth1 parent 1: protocol ipv6 u32 match ip6 flowlabel 0x54321 0xFFFFF flowid 1:2` - Attaches a filter to the root qdisc, directing traffic with flow label 0x54321 to the class with a rate of 200Mbps

You can check everything using:

- `tc qdisc show dev eth1`
- `tc class show dev eth1`
- `tc filter show dev eth1`

Exercise 2

Run the above sequence of 5 commands on `server1` `eth1` and ise `iperf3` on `client1` to verify against `iperf3` server running on `client2` (`fd00:3::40`):

- single instance of `iperf3` saturates full link speed
- single instance of `iperf3` with flow label set to 0x12345 (use `-L` option) reaches close to 100Mbps
- single instance of `iperf3` with flow label set to 0x54321 reaches close to 200Mbps

Commands

- `iperf3 -s --port 5202`
- `iperf3 -c fd00:3::40 --port 5202 -L 0x12345`

Exercise 3

Run 2 `iperf3` servers on `client2` on different ports (`--port`).

- verify that running 2 `iperf3` clients in parallel with **same** flow label keeps the total banwidth under previously set limits
- verify that running 2 `iperf3` clients in parallel with **different** flow labels makes it possible for both to reach 100Mbps/200Mbps at the same time


--- 


## IP Extension Headers [RFC](https://datatracker.ietf.org/doc/html/rfc2460#section-4)

The next 2 headers use the concept of **SecurityAssociation**. It is a fundamental concept that defines the security parameters and the keying material required for the secure communication between twh network entities. SAs are used to negotiate, establish, and manage the security attributes needed for the protection of IP packets.

Each SA is associated with specific security parameters that define how the IP packets will be secured:

- **Security protocol**: Specifies whether the Authentication Header (AH) or the Encapsulating Security Payload (ESP) is used.
- **Security Algorithm**: Specifises the cryptographic algorithms used.
- **Keying Material**: The shared secret key or keys used to secure the communication.
- **Lifetime**: Defines the duration for which the SA is valid.

### Authentication (AH)

```
     0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   | Next Header   |  Payload Len  |          RESERVED             |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                 Security Parameters Index (SPI)               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Sequence Number Field                      |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                                                               |
   +                Integrity Check Value-ICV (variable)           |
   |                                                               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

This header contains a cryptographic checksum (Integrity Check Value, ICV) computed over the immutable fields of IPv6 header, the payload and padding.

The purpose is to authenticate the packet and to ensure its integrity. It does not encrypt the payload.


### Encapsulation (ESP)

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ ----
|               Security Parameters Index (SPI)                 | ^Int.
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ |Cov-
|                      Sequence Number                          | |ered
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ | ----
|                    Payload Data* (variable)                   | |   ^
~                                                               ~ |   |
|                                                               | |Conf.
+               +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ |Cov-
|               |     Padding (0-255 bytes)                     | |ered*
+-+-+-+-+-+-+-+-+               +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ |   |
|                               |  Pad Length   | Next Header   | v   v
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ ------
|         Integrity Check Value-ICV   (variable)                |
~                                                               ~
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

Used to encrypt the payload and it can operate in 2 modes:

- **Transport mode** - Only the payload is encrypted, the IP header is untouched.
- **Tunnel mode** - The whole original IP packet is encrypted and put inside a new IP packet. (VPN standard)

### Hop by hop

```
     0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |  Next Header  |  Hdr Ext Len  |                               |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                               +
    |                                                               |
    .                                                               .
    .                            Options                            .
    .                                                               .
    |                                                               |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

he Hop-by-Hop Options header is used to carry optional information that must be examined by every node along a packet's delivery path. The Hop-by-Hop Options header is identified by a Next Header value of 0 in the IPv6 header, and has the following format:

However, it is to be expected that high-performance routers will either ignore it or assign packets containing it to a slow processing path.  Designers planning to use a hop-by-hop option need to be aware of this likely behaviour.