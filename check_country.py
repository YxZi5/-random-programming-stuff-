#!/bin/usr/python3
import subprocess as sp

adresy = open("out1.txt", "r")

for adres in adresy:
	adres = adres.strip()

	program = "geoiplookup"

	out = program + " " + adres
	ASN = sp.getoutput(out)

	print(f"{adres} - {ASN}")

adresy.close()