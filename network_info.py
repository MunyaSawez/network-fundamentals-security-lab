import socket

#get the computer's hostname
hostname = socket.gethostname()

#get the computer's IP address
ip_address = socket.gethostbyname(hostname)

print("====NETWORK INFORMATION TOOL====")
print("Hostname:", hostname)
print("IP address:", ip_address)

#perform a DNS lookup
domain = "google.com"

domain_ip = socket.gethostbyname(domain)

print("====DNS LOOKUP====")
print("Domain:", domain)
print("IP adress:", domain_ip)

try:
    socket.create_connection(("8.8.8.8",53), timeout=5)
    print("Internet connected")

except OSError:
    print("No Internet")

