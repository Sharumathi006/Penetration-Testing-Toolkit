import argparse
import sys
from modules import port_scanner, ssh_brute_forcer, dir_enumerator, banner_grabber

def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    subparsers = parser.add_subparsers(dest="module", required=True)

    # Port Scanner
    pscan = subparsers.add_parser("portscan", help="Scan open ports on a target")
    pscan.add_argument("target", help="Target IP or domain")
    pscan.add_argument("--ports", nargs="+", type=int, required=True, help="List of ports to scan")

    # SSH Brute-Forcer
    ssh = subparsers.add_parser("sshbrute", help="Brute-force SSH login")
    ssh.add_argument("host", help="SSH host")
    ssh.add_argument("user", help="SSH username")
    ssh.add_argument("password_file", help="Path to password wordlist file")

    # Directory Enumerator
    direnum = subparsers.add_parser("direnum", help="Enumerate hidden directories/paths")
    direnum.add_argument("url", help="Target URL (e.g., http://example.com/)")
    direnum.add_argument("wordlist_file", help="Path to directory wordlist")

    # Banner Grabber
    banner = subparsers.add_parser("banner", help="Grab service banner from an IP:port")
    banner.add_argument("ip", help="Target IP")
    banner.add_argument("port", type=int, help="Target Port")

    args = parser.parse_args()

    if args.module == "portscan":
        port_scanner.scan_ports(args.target, args.ports)

    elif args.module == "sshbrute":
        try:
            with open(args.password_file, "r") as f:
                passwords = f.read().splitlines()
            ssh_brute_forcer.brute_force_ssh(args.host, args.user, passwords)
        except FileNotFoundError:
            print(f"[!] Password file '{args.password_file}' not found.")
            sys.exit(1)

    elif args.module == "direnum":
        try:
            with open(args.wordlist_file, "r") as f:
                words = f.read().splitlines()
            dir_enumerator.enumerate_dirs(args.url, words)
        except FileNotFoundError:
            print(f"[!] Wordlist file '{args.wordlist_file}' not found.")
            sys.exit(1)

    elif args.module == "banner":
        banner_grabber.grab_banner(args.ip, args.port)

if __name__ == "__main__":
    main()
