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



def compileTCC(compiler, version, install = False):

	res = 0
	
	def checkReturn():
		if res == 0:
			print(GREEN + "PASSED" + RESET)
			return
		else:
			print(RED + "FAILED" + RESET)
			exit(1)

	print("")
	print(WHITE + "reconfiguring tinycc (just in case)" + RESET)

	# configure the compiler
	command = ["./configure", "--debug"]
	p = subprocess.Popen(command, cwd=version, stdout=subprocess.PIPE)
	
	for c in iter(lambda: p.stdout.read(1), b""):
		print(c.decode(), end="")
	p.wait()
	res = p.returncode 
	checkReturn()
	print("")
	
	print(CYAN + "making source version {:s} with {:s}".format(version, compiler) + RESET)
	
	# make is often sus, and i do not trust it. clean every time
	command = ["make", "clean"]
	p = subprocess.Popen(command, cwd=version, stdout=subprocess.PIPE)
	
	for c in iter(lambda: p.stdout.read(1), b""):
		print(c.decode(), end="")
	
	p.wait()
	res = p.returncode 
	checkReturn()
	
	command = ["make", "CC={:s}".format(compiler), "CPPFLAGS=-g", "-j8", "CFLAGS=-g -I/include/ -L."]
	p = subprocess.Popen(command, cwd=version, stdout=subprocess.DEVNULL)
	p.wait()
	res = p.returncode 
	
	command = ["sudo", "make", "install", "-j8", "CPPFLAGS=-g", "CFLAGS=-g"]
	p = subprocess.Popen(command, cwd=version, stdout=subprocess.PIPE)
	
	for c in iter(lambda: p.stdout.read(1), b""):
		print(c.decode(), end="")
	
	p.wait()
	res = p.returncode 
	checkReturn()
	print("")

	

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
	
	
	buggedVersion = "./tinycc-bugged/"
	cleanVersion = "./tinycc-clean/"
	
	compileTCC("gcc", buggedVersion)
	compileTCC("tcc", cleanVersion)
	
	# compile login.c 
	print(WHITE + "compiling login.c" + RESET)
	#command = ["tcc", "login.c", "-g", "-o", "buggedLogin", "-I", "./tinycc-bugged/include/", "-L", "./tinycc-bugged/"]
	command = ["tcc", "login.c", "-g", "-o", "buggedLogin"]
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
			# "curse" code
			print("test {:3d} {:s}{:>{width}s}{:s} PASSED {:s}with return code {:d}{:s}".format(i, WHITE, name, GREEN, RESET, processRes, RESET, width=width))
		else:
			print("test {:3d} {:s}{:>{width}s}{:s} FAILED {:s}with return code {:d}{:s}".format(i, WHITE, name, RED, RESET, processRes, RESET, width=width))
		
	
	print("")
	
	pass

if __name__ == "__main__":


	recompile()

	runTests()

	pass

