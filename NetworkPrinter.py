import sys
import yaml
from collections import defaultdict

def parse_compose(path):
    with open(path) as f:
        data = yaml.safe_load(f)
    return data.get("services", {})

def extract_nodes_and_edges(services):
    containers = {}
    network_edges = defaultdict(list)

    for name, config in services.items():
        networks = config.get("networks", {})
        if isinstance(networks, list):
            networks = {net: {} for net in networks}

        containers[name] = {}
        for net, net_cfg in networks.items():
            ip = net_cfg.get("ipv4_address") if isinstance(net_cfg, dict) else None
            containers[name][net] = ip
            network_edges[net].append(name)

    return containers, network_edges

def draw_graph(containers, network_edges):
    print("📦 Container-Based Network Topology:\n")

    for net, members in network_edges.items():
        if len(members) < 2:
            continue  # skip isolated containers
        for i in range(len(members)-1):
            a, b = members[i], members[i+1]
            a_ip = containers[a].get(net, "")
            b_ip = containers[b].get(net, "")
            print(f" 🐳 {a} ({a_ip})")
            print(f"    │")
            print(f"    ▼ {net}")
            print(f" 🐳 {b} ({b_ip})\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python draw_topology.py <docker-compose.yml>")
        sys.exit(1)

    services = parse_compose(sys.argv[1])
    containers, net_edges = extract_nodes_and_edges(services)
    draw_graph(containers, net_edges)

if __name__ == "__main__":
    main()
