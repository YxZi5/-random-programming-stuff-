#!/usr/bin/python3
import sys

def xor(byte, key):
	return (byte ^ key)

def parse_to_bytes(filename):
	byytes = []
	with open(filename, 'rb') as file:
		lines = file.read().splitlines()
		for line in lines:
			for byte in line:
				hex_byte = hex(byte)
				if hex_byte == '0x0':
					hex_byte = hex_byte+'0'
				elif len(hex_byte) != 4:
					hex_byte = f"0x0{hex_byte[2:]}"
				byytes.append(hex_byte)
		return byytes

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("usage: python3 xor.py <filename> <hex_key>")

	filename = sys.argv[1]
	byytes = parse_to_bytes(filename)

	# prepare key
	input_key = sys.argv[2]
	hex_key = f"0x{input_key}"
	key = int(hex_key, 16)
	
	output_string = ""

	# xor all bytes with entered key:
	for byte in byytes:
		byte = int(byte, 16)
		xored = xor(byte, key)

		# script will be display only printable ascii chars
		if xored >= 32 and xored <= 126:
			output_string += chr(xored)

	# print output as one string
	print(output_string)
