# Dynamic Store

`configd` daemon is responsible for the system configuration.
It monitors and maintains values in the Dynamic Store,
A key-value pairs database
containing the configuration settings and information about
the current system state.

Interfacing with Dynamic Store can be done through
the `SystemConfiguration.framework SCDynamicStore` APIs,
in rust [system-configuration crate](https://crates.io/crates/system-configuration)
or the `scutil` command.

```sh
scutil --dns # display dns configuration
scutil --nwi
scutil --get HostName # get hostname
sudo scutil --set HostName [name] # set the system hostname
scutil -r [host] # check network reachability (aka ping)
```

Enter interactive mode

```sh
scutil
> list
> show State:/Network/Global/IPv4
> show Setup:/Network/Global/DNS
```
