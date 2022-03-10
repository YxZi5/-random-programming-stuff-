#!/usr/bin/python3
import requests
import sys
import argparse

parser = argparse.ArgumentParser(description='Subdomain scanner')
parser.add_argument('--url', required=False, help='Remote Target (domain name) for example: google.com')
parser.add_argument('--wordlist', required=False, help='Path to the wordlist')
args = parser.parse_args()

with open(f"{args.wordlist}", "r") as subdomains:
	
	for subdomain in subdomains:
		subdomain = subdomain.strip()

		url = f"http://{subdomain}.{args.url}"

		try:
			response = requests.get(url) #wysłanie requesta do adresu (zmienna url)

			if response.status_code == 200:
				print(f"[+] {url}")
			elif response.status_code == 404:
				print(f"[-] {url}")

		except requests.ConnectionError:
			pass
			
	subdomains.close()