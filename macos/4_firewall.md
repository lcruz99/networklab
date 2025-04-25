# Firewalls

## Application level firewall

`socketfilterfw` is Apple’s Application Firewall,
which allows or blocks incoming connections at the app level.

GUI is at System Settings > Network > Firewall

```
/usr/libexec/ApplicationFirewall/socketfilterfw
```

## Packet Filter firewall

macOS uses an old fork of the OpenBSD `pf` stateful firewall.

Filter rules are evaluated in sequential order, first to last.
Unless the packet matches a rule containing the `quick` keyword,
the packet will be evaluated against all filter rules
before the final action is taken.

The last rule to match is the "winner" and
will dictate what action to take on the packet.

```bash
action [direction] [log] [quick] [on interface] [af] [proto protocol] 
[from src_addr [port src_port]] [to dst_addr [port dst_port]] 
[flags tcp_flags] [state]
```

Main configuration file is located at `/etc/pf.conf`.
We can use anchors to extend it.

The `pf.conf` file has seven parts:

- `macros`: User-defined variables that can hold IP addresses, interface
names, etc.
- `tables`: A structure used to hold lists of IP addresses.
- `options`: Various options to control how PF works.
- `scrub`: Reprocessing packets to normalize and defragment them.
- `translation`: Controls Network Address Translation and packet redirection.
- `filter rules`: Allows the selective filtering or blocking of packets
as they pass through any of the interfaces.

```bash
pfctl -e # enable
pfctl -d # disable

pfctl -f /etc/pf.conf # Load the pf.conf file
pfctl -nf /etc/pf.conf # Parse the file, but don't load it

pfctl -sn # Show the current NAT rules
pfctl -sr # Show the current filter rules
pfctl -ss # Show the current state table
pfctl -si # Show filter stats and counters
pfctl -sa # Show EVERYTHING it can show
```

Minimal config, that blocks all incoming traffic,
but allow traffic we make ourselves, retain state information on our connections.

Keeping state information allows return traffic
for all connections we have initiated.

```sh
block in all
pass out all # keep state by default
```

## Exercise

Block incoming ICMP packets.

Add the following to `pf.conf`

```sh
block in proto icmp
pass out all
block out proto icmp
```

And reload the config

## Logging

We can add the `log` keyword to rules, to enable logging.
But first we need to enable the `pflog0` interface and then do
a packet capture on it.

```sh
block log on en0 proto icmp
```

```sh
ifconfig pflog0 create
tcpdump -n -e -ttt -i pflog0
```
