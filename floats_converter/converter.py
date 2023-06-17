#!/usr/bin/python3

"""
przyklad przeliczania z decymalnej liczby zmiennoprzecinkowej na binarna dla liczby 0.2 i 4 bitow dlugosci liczby wyjsciowej:

0.2 * 2 = 0 i 0.4
0.4 * 2 = 0 i 0.8
0.8 * 2 = 1 i 0.6
0.6 * 2 = 1 i 0.2

"""
def dec_bin(number, num_of_bites):
	out = "0."
	k = 2
	for i in range(0, num_of_bites):
		o = number * k
		if o > 1:
			out += "1"
			number = float("0."+str(o)[2])
		else:
			out += str(o)[0]
			number = o

	return out

"""
Przeliczanie wartosci zmienno-przecinkowej z systemu binarnego
na decymalny przyklad dla 4 bitowej wartosci 0.2:

0 * 2**-1
0 * 2**-2
1 * 2**-3
1 * 2**-4

"""

def bin_dec(bin_number, num_of_bites):
	out = 0
	potega = -1
	bin_number = str(bin_number)[2:]
	for k in range(0, len(bin_number)):
		out += int(bin_number[k]) * 2**potega
		potega -= 1

	return out

if __name__ == '__main__':
	print("wartosc 0.2 zapisana binarnie zaleznie od ilosci bitow\n")
	print("Ilosc bitow | wartosc decymalna")

	bits = 4
	for i in range(0, 5):
		bytes_var = dec_bin(0.2, bits)
		print(f"{bits}           | {bin_dec(bytes_var, bits)}")
		bits = bits * 2

	# bytes4 = dec_bin(0.2, 4)
	# bytes8 = dec_bin(0.2, 8)
	# bytes16 = dec_bin(0.2, 16)

	# print(f"4           | {bin_dec(bytes4, 4)}")
	# print(f"8           | {bin_dec(bytes8, 8)}")
	# print(f"16          | {bin_dec(bytes16, 16)}")
