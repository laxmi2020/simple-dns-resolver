import socket

def dns_resolver(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Invalid domain name or unable to resolve."

domain_name = input("Enter the domain name: ")
resolved_ip = dns_resolver(domain_name)
print(f"The IP address of {domain_name} is: {resolved_ip}")
