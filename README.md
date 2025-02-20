# Network-lab Docker Compose Setup

This project sets up a **4-device network topology** using Docker Compose, where devices are connected as follows:

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

####  Build and Start the Network
```sh
docker-compose up --build -d
```

#### Test Communication Between Containers
```sh
docker exec -it networklab-client1-1 ping -c 3 networklab-client2-1
docker exec -it networklab-client1-1 ping -c 3 networklab-server1-1
docker exec -it networklab-client1-1 ping -c 3 networklab-server2-1
docker exec -it networklab-client2-1 ping -c 3 networklab-server2-1
docker exec -it networklab-client2-1 ping -c 3 networklab-server1-1
```

 #### Inspect Networks
 ```sh
 docker network ls
 docker network inspect net1
 ```

#### Stop containers
```sh
docker-compose down
```

#### Complete clean-up
```sh
docker-compose down --volumes --remove-orphans
docker system prune -a
```
