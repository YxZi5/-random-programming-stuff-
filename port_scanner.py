#!/usr/bin/python
import socket
import argparse

parser = argparse.ArgumentParser(description='TCP/UPD port scanner')
parser.add_argument('--ip', required=False, help='Remote Target (IP address)')
args = parser.parse_args()

print("Port Scanner")

ip = args.ip
ports = 1, 22, 80, 2, 135, 335, 445

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

for port in ports:
        response = portscanner(ip, port)

        if response == 0:
                print(f"port {port} is opened")
        else:
                print(f"port {port} is closed")                 