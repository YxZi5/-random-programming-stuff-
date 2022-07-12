#!/usr/bin/python
import socket
import argparse

parser = argparse.ArgumentParser(description='MINECRAFT PORT TCP/25565 SCANNER')
parser.add_argument('--ip', required=True, help='Remote Target (IP address)')
args = parser.parse_args()

print("Port Scanner")

ips = args.ip
port = 25565

def portscanner(ip, port, result = 1):
        try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                r = sock.connect_ex((ip, port))

                if r == 0:
                        result = r
                sock.close()

        except Exception as e:
                pass
        return result
outputfile = open("out.txt", "w")
with open(ips, "r") as addresses:
        addresses = addresses.read().splitlines()

        for addr in addresses:
                response = portscanner(addr, port)
                if response == 0:
                        print(f"[+] {addr} - posible minecraft server!")
                        outputfile.write(f"{addr}\n")
        addresses.close()
print(f"All possible minecraft servers was write in {outputfile}")