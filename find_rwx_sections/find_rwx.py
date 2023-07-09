#!/usr/bin/python3
import pefile
import sys

def find_image_base(exe_path):
	pe = pefile.PE(exe_path)
	output = pe.OPTIONAL_HEADER.ImageBase
	return hex(output)

def find_rwx_section(exe_path, baseaddr):
	pe = pefile.PE(exe_path)
	baseaddr = baseaddr[2:].upper()
	
	for section in pe.sections:
		section_name = section.Name.decode().strip('\x00')
		if section.IMAGE_SCN_MEM_READ and section.IMAGE_SCN_MEM_WRITE and section.IMAGE_SCN_MEM_EXECUTE:
			section_offset = hex(section.VirtualAddress)[2:].upper()
			section_address = f"0x{int(baseaddr)+int(section_offset)}"
			print(f"[+] file: {exe_path} | section RWX: {section_name} | address: {section_address}")

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("usage: find_rwx.py filename.exe")
		sys.exit()

	baseAddr = find_image_base(sys.argv[1])
	
	find_rwx_section(sys.argv[1], baseAddr)