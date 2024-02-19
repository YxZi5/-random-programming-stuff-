#!/usr/bin/python3
import sys

def toText(bytess):
	word = ""
	for char in bytess:
		char = chr(int(char, 16))
		word += char

	word = word[::-1]
	return word

def parse_hex_word(hex_word):
	bytess = []
	one_byte = ""

	for b in range(0, len(hex_word)):

		one_byte += hex_word[b]
		if len(one_byte) == 2:
			bytess.append(one_byte)
			one_byte = ""

	return bytess

if __name__ == '__main__':

	if len(sys.argv) != 2:
		print("usage: extr.py asm_code.asm")
		exit(-1)

	file = str(sys.argv[1])
	with open(file, "r") as asm_code:
		asm_code = asm_code.read().splitlines()

	hex_words = []
	for line in asm_code:
		if "0x" in line:
			
			h = str(line).split('0x')[1].split(" ")[0]
			if len(h) != 8:
				continue

			hex_words.append(h)

	for hex_word in hex_words:
		bytees = parse_hex_word(hex_word)
		print(f"hex value: {hex_word} | after conversion: {toText(bytees)}")

