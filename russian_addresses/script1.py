#!/usr/bin/python3
import os
import sys

def main():
	RU = 0
	USA = 0
	CHIN = 0
	with open("adresy.txt", "r") as addresses:
		for address in addresses:
			address = address.strip()

			prog = 'geoiplookup'
			cmd = f"{prog} {address}"

			result = os.popen(cmd).read()

			if "Russian" in result:
				RU += 1
			elif "United" in result:
				USA += 1
			elif "China" in result:
				CHIN += 1
		addresses.close()

		print(f"RUSSIA: {RU}\nUSA: {USA}\nCHINA: {CHIN}")

if __name__ == '__main__':
	main()
	sys.exit()