#!/usr/bin/python3
import sys

def convert_to_shellcode(filename):
	shellcode = "unsigned char shellcode[] = \n"
	with open(filename, 'rb') as binfile:
	  exe_content = binfile.read()
	  counter = 0
	  for char in range(0, len(exe_content)):
	  	hex_char = hex(exe_content[char])
	  	hex_value = hex_char.split('0x')[1]
	  	counter += 1
	  	if counter == 17:
	  		shellcode += '"\n'
	  		counter = 1

	  	if (len(str(hex_value))) <= 1:
	  		if counter == 1 or counter == 0:
	  			shellcode += '"'
	  		shellcode += f'\\x0{str(hex_value)}'
	  	else:
	  		if counter == 1 or counter == 0:
	  			shellcode += '"'
	  		shellcode += f"\\x{str(hex_value)}"

	  	if char == len(exe_content)-1:
	  		shellcode += '";'
	  binfile.close()
	return shellcode

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print(f"Usage: {sys.argv[0]} filename.exe")
		sys.exit()
	print(convert_to_shellcode(sys.argv[1]))
