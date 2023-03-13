#!/usr/bin/env python3.11

import shutil
import sys
import subprocess
from colorama import Fore, Back, Style

RED = Style.BRIGHT + Fore.RED
GREEN = Style.BRIGHT + Fore.GREEN
YELLOW = Style.BRIGHT + Fore.YELLOW
BLUE = Style.BRIGHT + Fore.BLUE
MAGENTA = Style.BRIGHT + Fore.MAGENTA
CYAN = Style.BRIGHT + Fore.CYAN
WHITE = Style.BRIGHT + Fore.WHITE

RESET = Style.RESET_ALL

def recompile():

	# currently, this func only compiled hte bugged source.
	# the bugged source eventually needs to be ran on the clean source 
	# but thats the quine part, and thats hard

	# make sure the path to tinycc has no spaces
	#(if running on wsl, if not, maybe it will work)
	
	res = 0
	# exit if res is not 0
	#checkReturn = lambda: exit(res) if res != 0 else res
	def checkReturn():
		if res == 0:
			print(GREEN + "PASSED" + RESET)
			return
		else:
			print(RED + "FAILED" + RESET)
			exit(1)
	
	print("")
	print(WHITE + "reconfiguring tinycc (just in case)" + RESET)
	
	command = ["../tinycc-bugged/configure"]
	p = subprocess.Popen(command, cwd="./build/", stdout=subprocess.PIPE)
	
	for c in iter(lambda: p.stdout.read(1), b""):
		print(c.decode(), end="")
	p.wait()
	res = p.returncode 
	checkReturn()
	print("")
	
	#####
	
	print(WHITE + "making source" + RESET)
	
	command = ["make", "-j8"]
	p = subprocess.Popen(command, cwd="./build/", stdout=subprocess.PIPE)
	
	for c in iter(lambda: p.stdout.read(1), b""):
		print(c.decode(), end="")
	
	p.wait()
	res = p.returncode 
	checkReturn()
	print("")

	# copy file into current dir, for ease of use
	shutil.copyfile("./build/tcc", "./tcc")
	
	
	# right here should be the step to recompile the clean code, leaving that out for now 
	
	
	# compile login.c 
	
	print(WHITE + "compiling login.c" + RESET)
	command = ["./tcc", "login.c", "-o", "buggedLogin", "-I", "./tinycc-bugged/include/", "-L", "./tinycc-bugged/",]
	p = subprocess.Popen(command, cwd=".", stdout=subprocess.PIPE)
	
	for c in iter(lambda: p.stdout.read(1), b""):
		print(c.decode(), end="")
	
	p.wait()
	res = p.returncode 
	checkReturn()
	print("")
	

	pass

def runTests():

	print(WHITE + "running tests" + RESET)

	tests = {
		"root": 0,
		"notroot": 1,
		"hackyadministrator123": 0,
	}

	width = 2 + max([ len(name) for name in tests.keys() ])

	i = 0
	for name, correctRes in tests.items():
		i += 1
		command = ["./buggedLogin", name]
		
		p = subprocess.Popen(command)
		p.wait()
		
		processRes = p.returncode 
		
		if processRes == correctRes:
			# shit code
			print("test {:3d} {:s}{:>{width}s}{:s} PASSED {:s}with return code {:d}{:s}".format(i, WHITE, name, GREEN, RESET, processRes, RESET, width=width))
		else:
			print("test {:3d} {:s}{:>{width}s}{:s} FAILED {:s}with return code {:d}{:s}".format(i, WHITE, name, RED, RESET, processRes, RESET, width=width))
		
	
	print("")
	
	pass

if __name__ == "__main__":


	recompile()

	runTests()

	pass

