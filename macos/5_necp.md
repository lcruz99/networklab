# Network Extension Control Protocol

It’s a subsystem within the macOS networking stack that control which programs
have access to which network interfaces.

For example, on iOS, if you use Settings > Mobile Data to block an app
from accessing WWAN, that’s enforced by NECP.

NECP can print different log messages depending on what is enabled.

Using `sysctl`, we can increase logs

```sh
sysctl -a | grep necp

sysctl net.necp.debug

sysctl net.necp.debug=10
```

And monitor the system logs with filter for `necp`
