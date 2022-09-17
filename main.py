from stem import Signal
from stem.control import Controller
import os
import sys
import argparse
import requests

timex = 0
passwd = "th04"

def changer():
	with Controller.from_port(port=9051) as controller:
		controller.authenticate(password=passwd)
		controller.signal(Signal.NEWNYM)
		response = requests.get('https://api.myip.com/', proxies={'https': '127.0.0.1:8118'})
		ip_info = response.json()
		print("\n"+"[*] Your New Ip '"+ip_info["ip"]+"'")
		print("[*] Country '"+ip_info["country"]+"'")
		print("[*] Country Code '"+ip_info["cc"]+"'")		

class bcolors:

	BLUE = '\033[94m'
	GREEN = '\033[92m'
	RED = '\033[31m'
	YELLOW = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	BGRED = '\033[41m'
	WHITE = '\033[37m'

response = requests.get('http://icanhazip.com/', proxies={'http': '127.0.0.1:8118'})
norm_ip = response.text.strip()
print("[*] Your Ip Adress Is '"+norm_ip+"'")


clrs = bcolors()

if os.popen('whoami').read()  != "root":
	print("Please Run This Software On Root Account")
	sys.exit()

if os.name  != "posix":
	print("Work On Only Linux System!")
	sys.exit()

if __name__ != "__main__":
	sys.exit()


banner = """
######## ##     ##   #####   ##        
   ##    ##     ##  ##   ##  ##    ##  
   ##    ##     ## ##     ## ##    ##  
   ##    ######### ##     ## ##    ##  
   ##    ##     ## ##     ## ######### 
   ##    ##     ##  ##   ##        ##  
   ##    ##     ##   #####         ##    v3.43

usage: th04.py [-h] [-c]

TH04 (C) - @cyberm0n

optional arguments:
  -h, --help    show this help message and exit
  -c, --change  change your ip adress via tor
"""

parser = argparse.ArgumentParser(description="TH04 (C) - @cyberm0n ")
parser.add_argument("-t","--time",metavar="<second>",help="do loop via time",default="_")
group = parser.add_mutually_exclusive_group()
group.add_argument("-c","--change",help="change your ip adress via tor",action='store_true')
args = parser.parse_args()

if args.time != "_":
	timex = args.time

if args.change != True:
	time.sleep(timex)
	changer()


