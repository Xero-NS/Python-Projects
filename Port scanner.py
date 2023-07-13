import socket

target = input("Enter the IP address to scan: ")

# This function takes a port number as an argument and returns True if the port is open
def is_port_open(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((target, port))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()

# Scan all ports from 1 to 1024 and print the open ones
for port in range(1, 1025):
    if is_port_open(port):
        print(f"Port {port} is open")
