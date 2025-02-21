#!/bin/bash

containers=$(docker ps --format '{{.Names}}' | grep networklab-*)

echo "Testing connectivity between all containers..."
echo "-------------------------------------------"

for src in $containers; do
    echo "From $src:"
    for dst in $containers; do
        if [[ "$src" != "$dst" ]]; then
            docker exec "$src" ping -c 2 "$dst" &>/dev/null
            
            if [[ $? -eq 0 ]]; then
                echo "  Can reach $dst"
            else
                echo "  Cannot reach $dst"
            fi
        fi
    done
    echo "-------------------------------------------"
done
