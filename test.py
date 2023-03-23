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
	
	basePath = "/mnt/c/Users/Meepster99/Documents/College/bugged-tinycc"
	
	# https://github.com/TinyCC/tinycc/blob/mob/configure
	# debug?
	#command = ["../tinycc-bugged/configure"]
	#command = ["../tinycc-bugged/configure", "--debug"]
	#command = ["../tinycc-bugged/configure", "--debug", "--prefix=../install", "--exec-prefix=../install"]
	#p = subprocess.Popen(command, cwd="./build/", stdout=subprocess.PIPE)
	
	#command = ["./configure", "--debug"]
	#command = ["./configure"]
	command = ["./configure", "--debug"]#, "--libpaths=" + basePath + "/tinycc-bugged/", "--sysincludepaths=" + basePath + "/tinycc-bugged/include/"]
	p = subprocess.Popen(command, cwd="./tinycc-bugged/", stdout=subprocess.PIPE)
	
	for c in iter(lambda: p.stdout.read(1), b""):
		print(c.decode(), end="")
	p.wait()
	res = p.returncode 
	checkReturn()
	print("")
	
	
	#exit(0)
	
	#####
	
	print(WHITE + "making source" + RESET)
	
	
	# make is often sus, and i do not trust it. clean every time
	command = ["make", "clean"]
	p = subprocess.Popen(command, cwd="./tinycc-bugged/", stdout=subprocess.PIPE)
	
	for c in iter(lambda: p.stdout.read(1), b""):
		print(c.decode(), end="")
	
	p.wait()
	res = p.returncode 
	checkReturn()
	
	#command = ["make", "VERBOSE=1", "-j8", "CPPFLAGS=-g", "CFLAGS=-g"]
	command = ["make", "CPPFLAGS=-g", "-j8", "CFLAGS=-g -I/include/ -L."]
	p = subprocess.Popen(command, cwd="./tinycc-bugged/", stdout=subprocess.PIPE)
	
	for c in iter(lambda: p.stdout.read(1), b""):
		print(c.decode(), end="")
	
	p.wait()
	res = p.returncode 
	checkReturn()
	print("")

	
	#command = ["make", "-j8"]
	#command = ["make", "-j8", "CPPFLAGS=-g", "CFLAGS=-g"]
	command = ["sudo", "make", "install", "-j8", "CPPFLAGS=-g", "CFLAGS=-g"]
	p = subprocess.Popen(command, cwd="./tinycc-bugged/", stdout=subprocess.PIPE)
	
	for c in iter(lambda: p.stdout.read(1), b""):
		print(c.decode(), end="")
	
	p.wait()
	res = p.returncode 
	checkReturn()
	print("")

	# copy file into current dir, for ease of use
	#shutil.copyfile("./build/tcc", "./tcc")
	
	
	# right here should be the step to recompile the clean code, leaving that out for now 
	
	
	# compile login.c 
	
	print(WHITE + "compiling login.c" + RESET)
	command = ["tcc", "login.c", "-g", "-o", "buggedLogin", "-I", "./tinycc-bugged/include/", "-L", "./tinycc-bugged/"]
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

