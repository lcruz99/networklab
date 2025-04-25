# Honorable Mentions

## Open unverified software

```sh
sudo spctl --master-disable
# launch untrusted app
sudo spctl --master-enable
```

## Airport

Deprecated tool that could be used to enter monitoring mode and  sniff network traffic.

```sh
sudo /System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport en1 sniff 2g1/20

# Show interface information
sudo /System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -I
```

## Network Quality / Speed test

```sh
networkQuality -v
```

## Network

Configuration tool for System Preferences network settings.

```sh
networksetup -listallnetworkservices
networksetup -listallhardwareports

networkservice -getinfo networkservice
```

## Enable SSH

```sh
sudo systemsetup -setremotelogin on
# Check status
sudo systemsetup -getremotelogin
```
