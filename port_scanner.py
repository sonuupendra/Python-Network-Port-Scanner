import nmap

nm = nmap.PortScanner()

target = "45.33.32.156"
options = "-sV -sC"

nm.scan(target, arguments=options)

for host in nm.all_hosts():
    print(f"Host: {host} ({nm[host].hostname()})")
    print("State:", nm[host].state())

    for protocol in nm[host].all_protocols():
        print("Protocol:", protocol)
        port_info = nm[host][protocol]

        for port in sorted(port_info.keys()):
            data = port_info[port]
            print(f"Port: {port}\tState: {data['state']}")