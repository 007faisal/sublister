import socket

def find_subdomains(domain):
    subdomains = []
    with open("word.txt", "r") as wordlist:
        for line in wordlist:
            subdomain = line.strip() + "." + domain
            try:
                # Try to resolve the subdomain
                ip = socket.gethostbyname(subdomain)
                subdomains.append(subdomain)
                print(f"{subdomain} resolves to {ip}")
            except socket.error:
                pass
    return subdomains

domain = input("Enter a domain: ")
subdomains = find_subdomains(domain)
print(f"Found {len(subdomains)} subdomains: {subdomains}")
