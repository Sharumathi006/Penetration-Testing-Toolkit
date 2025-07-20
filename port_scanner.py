import socket

def scan_ports(target, ports):
    print(f"[+] Scanning {target} on ports: {ports}")
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((target, port))
            print(f"[+] Port {port} is open")
            open_ports.append(port)
            sock.close()
        except:
            pass
    return open_ports
