#!/usr/bin/python3
import argparse
import requests

parser = argparse.ArgumentParser(description='XSS vulnerability scanner')
parser.add_argument('--url', required=False, help='Remote Target (url address)')
args = parser.parse_args()

url_parametr = args.url
user_agent = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.7.10) Gecko/20050717 Firefox/1.0.6'}

def load_events():
	with open("payloads.txt", "r") as events:
		events = events.read().split('\n')

	return events

if __name__ == '__main__':
	events = load_events()

	for payload in events:
		url = f"{url_parametr}{payload}"
		
		req = requests.get(url, headers=user_agent)

		if "<" in payload or ">" in payload or "</" in payload:
			if payload in req.text:
				print("Vulnerable")
			else:
				print("Secure")
		else:
			print("Secure")