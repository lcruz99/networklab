import docker
import subprocess

containers = {
    "host1": "net1",
    "server1": ["net1", "net2"],
    "server2": ["net2", "net3"],
    "host2": "net3",
}

client = docker.from_env()

def get_container_ip(container_name, network_name):
    try:
        container = client.containers.get(container_name)
        return container.attrs["NetworkSettings"]["Networks"][network_name]["IPAddress"]
    except KeyError:
        return None
    except Exception as e:
        print(f"Error getting IP for {container_name} on {network_name}: {e}")
        return None

def test_ping(source, target, target_ip):
    print(f"Testing connectivity: {source} → {target} ({target_ip})")
    cmd = ["docker", "exec", source, "ping", "-c", "3", target_ip]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.returncode == 0:
        print(f"SUCCESS: {source} can reach {target}")
    else:
        print(f"FAILURE: {source} cannot reach {target}")
        print(result.stderr)

def main():
    print("\nStarting connectivity tests...\n")
    
    for src, src_nets in containers.items():
        if not isinstance(src_nets, list):
            src_nets = [src_nets]
        
        for dst, dst_nets in containers.items():
            if src == dst:
                continue
            
            common_net = list(set(src_nets) & set(dst_nets))
            if common_net:
                target_ip = get_container_ip(dst, common_net[0])
                if target_ip:
                    test_ping(src, dst, target_ip)

    print("\nAll tests completed.")

if __name__ == "__main__":
    main()