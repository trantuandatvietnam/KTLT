import dns.resolver

my_resolver = dns.resolver.Resolver()

hosts = ["google.com", "facebook.com"]

for host in hosts:
    print(host)
    ip = my_resolver.resolve(host, "A")
    for i in ip:
        print(i)