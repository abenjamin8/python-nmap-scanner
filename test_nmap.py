# Author: Adam Benjamin (https://github.com/abenjamin8)
# Project: python-nmap-scanner

import nmap

scanner = nmap.PortScanner()
scanner.scan('127.0.0.1', '1-1024')

for host in scanner.all_hosts():
    print(f"Host: {host}")
    print(f"State: {scanner[host].state()}")

    for proto in scanner[host].all_protocols():
        ports = scanner[host][proto].keys()
        for port in ports:
            state = scanner[host][proto][port]['state']
            print(f"  {proto} port {port}: {state}")