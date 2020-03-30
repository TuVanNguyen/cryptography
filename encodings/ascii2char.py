#!/usr/bin/python3.7

import sys

def ascii2char(asciiString):
	asciiNum = asciiString.split(',')
	plaintext = "".join(chr(int(ascii)) for ascii in asciiNum)
	print(plaintext)

def main():
	ascii2char(sys.argv[1])

if __name__=="__main__":
	main()
