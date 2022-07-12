#!/usr/bin/python3
from mcstatus import JavaServer
import sys
import socket
import argparse
import time

parser = argparse.ArgumentParser(description='Minecraft server scanner')
parser.add_argument('-i', '--inputfile', type=str, required=True, help='put here the list of target servers')
parser.add_argument('-o', '--outputfile', type=str, required=True, help='In this file scanner will write output values')
args = parser.parse_args()

inputfile = args.inputfile
outputfile = args.outputfile

def len_of_addr(addr):
	l = len(addr)

	if l > 15:
		return False

	if l <= 15:
		return True

def check_server(addr, port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		r = sock.connect_ex((addr, port))

		if r == 0:
			return "[+] Available"
		else:
			return "[-] Not available"
		sock.close()
	except Exception as e:
		pass

if __name__ == '__main__':
	mc_port = 25565
	out_file = open(outputfile, "w")

	with open(inputfile, "r") as file:
		lines = file.read().splitlines()
	for linia in lines:
		linia = linia.strip()
		ip = linia

		s = check_server(ip, mc_port)

		if len_of_addr(ip) == True:
			try:
				server = JavaServer(ip, mc_port)
				status = server.status()
				version = str(status.version.name)
				p = status.players.online

				output = (f"{ip} - {s} - version of game: {version} - players online: {p}")
				print(output)
				out_file.write(f"{output}\n")
			except:
				print(f"Failed to get status of: {ip}")
				continue
	print(f"\n[+] The output values are also in the {outputfile}")