# mDNS Responder

Is a daemon that handles multicast DNS, Bonjour services, and standard DNS resolution.

Used mostly by Apples APIs, commands like `dig` or `nslookup` bypass it.

## Caching

Caches responses until some of the network configuration changes are noticed by `configd`.

To manually flush cache, send -HUP signal to the process.

```sh
sudo killall -HUP mDNSResponder
```

## Logging

To enable more detail logging send `USR1` and `USR2` signal to
the process (`kill -s USR1 <PID>`) and use `log` commands.

```sh
log stream --predicate 'process == "mDNSResponder"' --info

sudo tcpdump -i any -nn -v port 53
nslookup google.com
```

Navigate to `google.com` in Safari
