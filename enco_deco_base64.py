#!/bin/usr/python3
#this script is intended for linux systems
import base64
import os

def encoding():
	widomosc = input("Type the message what you want encrypt: ")
	wiadomosc_bytes = widomosc.encode('ascii')
	base64_bytes = base64.b64encode(wiadomosc_bytes)
	base64_wiadomosc = base64_bytes.decode('ascii')

	print(base64_wiadomosc)

def decoding():
	base64_message = input("Type the message what you want decode: ")
	base64_bytes = base64_message.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	message = message_bytes.decode('ascii')

	print(message)

print(
	"What you want to do:\n",
	"1.Encoding\n",
	"2.Decoding\n",
	"3.exit from the program\n"
	)

zmienna = int(input("Type here: "))

if zmienna == 1:
	os.system('clear')
	encoding()
elif zmienna == 2:
	os.system("clear")
	decoding()
else:
	exit()