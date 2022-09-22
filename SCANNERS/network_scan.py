#!/usr/bin/python3
from scapy.all import *
import argparse
import os
import sys

def scan(ip):
	cmd = f"ping -c 1 -t 1 -W 1 {ip}"
	output = os.popen(cmd).read()

	searched = "ttl=64"

	if searched in output:
		return True
	else:
		return False

def create_list(addr, r):
	network_addr = str(addr[:-1])
	addresses = []
	for i in range(0, r):
		addresses.append(network_addr + str(i+1))

	return addresses
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-a', '--address', help='Target network ip')
	parser.add_argument('-r', '--range', help='number of addresses to scan')
	arguments = parser.parse_args()

	if not arguments.address or not arguments.range:
		parser.error(f"[-] Please specify an network IP and range")

	adresy = create_list(arguments.address, int(arguments.range))

	for addr in adresy:
		scanning = scan(addr)

		if scanning == True:
			print(f"{addr} - HOST IS UP [+]")
		else:
			print(f"{addr} - HOST IS DOWN [-]")


		