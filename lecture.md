# Linux TCP Source Code Intro

# Delivery to higher level handler
Socket structure stores everything about the socket, including the protocol and it's handler
https://elixir.bootlin.com/linux/v6.12.6/source/include/net/sock.h#L182

Handler are stored at
https://elixir.bootlin.com/linux/v6.12.6/source/net/ipv4/protocol.c#L27
And then extracted at
https://elixir.bootlin.com/linux/v6.12.6/source/net/ipv4/ip_input.c#L195
and invoked at
https://elixir.bootlin.com/linux/v6.12.6/source/net/ipv4/ip_input.c#L205

Handlers are registered at
ICMP - https://elixir.bootlin.com/linux/v6.12.6/source/net/ipv4/af_inet.c#L1940
TCP - https://elixir.bootlin.com/linux/v6.12.6/source/net/ipv4/af_inet.c#L1957
UDP - https://elixir.bootlin.com/linux/v6.12.6/source/net/ipv4/af_inet.c#L1948

Interesting detail: We can see that if there's no protocol handler registerd, ICMP destination unreachable is returned:
https://elixir.bootlin.com/linux/v6.12.6/source/net/ipv4/ip_input.c#L216


Here's the TCP handler itself for when we receive TCP packet:
https://elixir.bootlin.com/linux/v6.12.6/source/net/ipv4/tcp_ipv4.c#L2177

And here is the entrypoint when we connect:
https://elixir.bootlin.com/linux/v6.12.6/source/net/ipv4/tcp_ipv4.c#L218



# TCP 3way Handshake
TCP handshake is called a three-way handshake, where peer A communicates with B like:
A -> SYN -> B
A <- SYN + ACK <- B
A -> ACK -> B

We can correlate this to the TCP states enum defined in
https://elixir.bootlin.com/linux/v6.12.6/source/include/net/tcp_states.h#L18
Original TCP RFC describes the states very nicely:
https://datatracker.ietf.org/doc/html/rfc793

TCP_ESTABLISHED (1) The three-way handshake has completed; data can flow in both directions.
TCP_SYN_SENT (2)    The active opener (client) has sent a SYN and is waiting for SYN + ACK.
TCP_SYN_RECV (3)    The passive opener (server) has received a SYN, replied with SYN + ACK, and is waiting for the final ACK that finishes the handshake.
TCP_FIN_WAIT1 (4)   Local endpoint has initiated an active close by sending FIN; awaiting either an ACK of that FIN or a simultaneous FIN from the peer.
TCP_FIN_WAIT2 (5)   The ACK for our FIN has arrived; we now wait for the peer’s FIN.
TCP_CLOSE (7)   No connection exists (initial state, or fully torn down).
TCP_LISTEN (10) Passive open: the socket is bound and listening for incoming SYNs.

States differ based on POV - if we're the cient we emit SYN and final ACK and if we're the server then we just receive SYN and return SYNACK and immediately
call the state established.

# Experiment for
Track state setting by doing:
```
sudo perf record -ae 'sock:inet_sock_set_state' --call-graph dwarf
[do the experiment]
sudo perf script
```

and observe the stacktraces and states. You will see old state and new state being outputted.

# FUN read
tcp_collapse is the GC of TCP:
https://blog.cloudflare.com/the-story-of-one-latency-spike/
https://elixir.bootlin.com/linux/v6.12.6/source/net/ipv4/tcp_input.c#L5407

# Homework
Pick one of the following functions in TCP source code. These are present after installing `linux-perf` in `default` Libtelio vagrant VM:
```
vagrant@bookworm:~$ sudo perf list | grep 'tcp:'
  mptcp:ack_update_msk                               [Tracepoint event]
  mptcp:get_mapping_status                           [Tracepoint event]
  mptcp:mptcp_sendmsg_frag                           [Tracepoint event]
  mptcp:mptcp_subflow_get_send                       [Tracepoint event]
  mptcp:subflow_check_data_avail                     [Tracepoint event]
  tcp:tcp_bad_csum                                   [Tracepoint event]
  tcp:tcp_cong_state_set                             [Tracepoint event]
  tcp:tcp_destroy_sock                               [Tracepoint event]
  tcp:tcp_probe                                      [Tracepoint event]
  tcp:tcp_rcv_space_adjust                           [Tracepoint event]
  tcp:tcp_receive_reset                              [Tracepoint event]
  tcp:tcp_retransmit_skb                             [Tracepoint event]
  tcp:tcp_retransmit_synack                          [Tracepoint event]
  tcp:tcp_send_reset                                 [Tracepoint event]
```

Find a way to capture the event deterministically and share the findings.