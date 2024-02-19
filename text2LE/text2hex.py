#!/usr/bin/python3
import sys

# inp = "calc.exe"
if len(sys.argv) != 2:
	print("usage: text2hex.py string")
	sys.exit()

inp = sys.argv[1]
inp = inp[::-1]

chunks = []
chunk = ''

for i in range(0, len(inp)):
	chunk += inp[i]
	
	if len(chunk) >= 4:
		chunks.append(chunk)
		chunk = ""

for ch in chunks:

	hex_string = ""
	for k in range(0, len(ch)):
		dec_num = ord(ch[k])

		if k == 0:
			hex_string += hex(dec_num)
		else:
			hex_string += hex(dec_num)[2::]

	print(hex_string)
	hex_string = ""