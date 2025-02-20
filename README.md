# Network-lab Docker Compose Setup

This repository sets up a **4-device network topology** using Docker Compose, where devices are connected as follows:

```
      ┌──────────────────────────────────────────── net4 ─────────────────────────────────────────────┐
      │                                         172.23.0.0/16                                         │
      │                                                                                               │
      │                                                                                               │
      │                                                                                               │
      │                                                                                               │
┌─────┴─────┐                   ┌───────────┐                   ┌───────────┐                   ┌─────┴─────┐
│           │                   │           │                   │           │                   │           │
│  client1  ├────── net1 ───────┤  server1  ├────── net2 ───────┤  server2  ├────── net3 ───────┤  client2  │
│           │   172.20.0.0/16   │           │   172.21.0.0/16   │           │   172.22.0.0/16   │           │
└───────────┘                   └───────────┘                   └───────────┘                   └───────────┘
  172.20.0.2                      172.20.0.3                      172.21.0.4                      172.22.0.5
  172.23.0.2                      172.21.0.3                      172.22.0.4                      172.23.0.5
```
Each device runs a **lightweight Ubuntu-based container** with essential networking tools pre-installed.
(If a package is missing, add it to the Dockerfile and create a PR)

---

## Setup & Usage

####  Build and start the network
```sh
docker compose up [--build] -d
```

#### Stop containers
```sh
docker compose down
```

#### Complete clean-up
```sh
docker compose down --volumes --remove-orphans --rmi all
```

#### Run a command on a container
```sh
docker exec <container_name> <cmd>
```

####  Launch an interactive terminal on a container
```sh
docker exec -it <container_name> bash
```

 #### Inspect Networks
 ```sh
 docker network ls
 docker network inspect <network_name>
 ```
