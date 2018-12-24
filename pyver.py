#!/usr/bin/python3
from subprocess import Popen, PIPE
import requests, argparse, sys

sh = lambda cmd: Popen(cmd, stdout=PIPE, shell=True).communicate()[0]

def localver(name):
	ln = sh("pip3 freeze | grep "+name).decode().strip()
	if ln == "":
		return False
	else:
		return ln.split("==")[1].split("\n")[0]

def parse_args():
	p = argparse.ArgumentParser()
	p.add_argument(
		"package",
		help=("Package name. Eg: requests"))
	return p.parse_args()
def main(args):
	l = localver(args.package)
	try:
		g = requests.get("https://pypi.python.org/pypi/%s/json" % args.package).json()['info']['version']
	except Exception as e:
		print("[!]",e)
		print("[!] Package might not exist or your internet connection might be having issues")
		return None
	if not l:
		print("[!] Package is not installed locally")
		print("Global ver:",g)
	else:
		print("Local ver:",l)
		print("Global ver:",g)
if __name__ == "__main__":
	main(parse_args())
