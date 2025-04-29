#! /usr/bin/python3

import subprocess 

def cpu_available():
    try:
        kubectl_get_nodes_cmd = 'kubectl get nodes'
        node_info = subprocess.run(kubectl_get_nodes_cmd, shell=True, stdout=subprocess.PIPE) 
        node_lines = node_info.stdout.decode().strip().split('\n')[1:]
        node_names = [line.split()[0] for line in node_lines]
        
        for node_name in node_names:
            awk = "awk '{ print $3 }' | sed 's/%//' | grep -o '[0-9]*'"
            cpu_cmd = f"kubectl describe node {node_name} | grep -i allocated -A5 | grep -i cpu | {awk}"     
            output = subprocess.run(cpu_cmd, shell=True, stdout=subprocess.PIPE)
            value = output.stdout.decode()
            if value:
                value = int(value)
                threshold = 95
                if value >= threshold:
                    print(f"Node Available CPU - {node_name} allocated CPU is more than 95%: Allocated CPU: {value}%")
                else:
                    print(f"Node Available CPU - {node_name} allocated CPU is less than 95%: Allocated CPU: {value}%")
            else:
                print("Node Available CPU - No Output")
    except Exception as exc:
        print(exc)

cpu_available()