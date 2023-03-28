import nmap

nm = nmap.PortScanner()
portList = "21, 22, 23, 25, 80"
nm.scan('facebook.com', portList)
print(nm.all_hosts())
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

for host, status in hosts_list:
    print(host, status)
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        listport = nm[host]['tcp'].keys()
        for port in listport:
            print("Port: %s State: %s" % (port, nm[host][protocol][port]['state']))