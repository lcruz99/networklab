# Launch agents

`launchd` handles running processes, daemons and agents.

Agents and daemons are defined in XML format `.plist` files located in 5 places.

Agents are per-user programs started when a user logins.
Daemons system wide services are run on boot.

| Type | Location | Run as |
| ------------- | -------------- | -------------- |
| User Agents | `~/Library/LaunchAgents` | logged in user |
| Global Agents | `/Library/LaunchAgents` | logged in user |
| Global Daemons | `/Library/LaunchDaemons` | root |
| System Agents | `/System/Library/LaunchAgents` | logged in user |
| System Daemons | `/System/Library/LaunchDaemons` | root |

As a user you can not directly interact with `launchd`, but through `launchctl`

```sh
sudo launchctl list # list of all loaded agents
sudo launchctl load script.plist # activate a new agent
sudo launchctl unload scritp.plist # deactivate a loaded agent
sudo launchctl stop [script_file] # stop a running agent
```

## Exercise

Run `iperf3` server as a daemon.

Create an `com.local.iperf3.plist` file in `/Library/LaunchDaemons/`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" 
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.local.iperf3</string>

    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/iperf3</string>
        <string>-s</string>
    </array>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>StandardOutPath</key>
    <string>/var/log/iperf3.out</string>

    <key>StandardErrorPath</key>
    <string>/var/log/iperf3.err</string>
</dict>
</plist>
```

Set the file permissions

```sh
sudo chown root:wheel /Library/LaunchDaemons/com.local.iperf3.plist
sudo chmod 644 /Library/LaunchDaemons/com.local.iperf3.plist
```

Load the daemon

```sh
sudo launchctl load -w /Library/LaunchDaemons/com.local.iperf3.plist
sudo launchctl list | grep iperf3
```
