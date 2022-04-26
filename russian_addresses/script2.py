#!/usr/bin/python3
import os
import sys

def main():
	with open("adresy.txt", "r") as addresses:
		for address in addresses:
			address = address.strip()

			prog = 'geoiplookup'
			cmd = f"{prog} {address}"

			result = os.popen(cmd).read()
			if "Russian" in result:
				print(address)
				
		addresses.close()
if __name__ == '__main__':
	main()
	sys.exit()