#!/usr/bin/python3.7

import sys
import urllib.parse

def decodeurl(encodedtext):
	return urllib.parse.unquote(encodedtext)

def main():
	encodedFileName = sys.argv[1]
	encodedFile = open(encodedFileName, "r")
	encodedString = encodedFile.read() 
	print(decodeurl(encodedString))
	encodedFile.close()

if __name__ == "__main__":
	main()
