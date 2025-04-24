# Launch agents

`launchd` handles running processes, daemons and agents.

Agents and daemons are defined in `.plist` files located in 5 places.

Agents are started when a user logins.
Daemons are on system boot.

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
```
