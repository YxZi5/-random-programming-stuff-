#!/usr/bin/python3
import sys
import requests
import argparse 

parser = argparse.ArgumentParser(description='URL addresses scaner')
parser.add_argument('--url', required=False, help='Remote Target (url address)')
parser.add_argument('--wordlist', required=False, help='Path to the wordlist')
args = parser.parse_args()

user_agent = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.7.10) Gecko/20050717 Firefox/1.0.6'}

with open(f"{args.wordlist}", "r") as slownik:
	for slowo in slownik:
		slowo = slowo.strip()
		adres = args.url

		url = f"{adres}{slowo}"

		try:
			response = requests.get(url, headers=user_agent)

			if response.status_code == 200:
				print(f"[+] {url}")
			#elif response.status_code == 404:
			#	print(f"[-] {url}")
		except requests.ConnectionError:
			pass
	slownik.close()