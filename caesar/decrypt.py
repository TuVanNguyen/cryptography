#!/usr/bin/python3.7

import sys

def decrypt(ciphertext):
	ciphertext = ciphertext.upper()
	for shift in range(1,26):
		decrypttext = "".join(chr((ord(char) - 65  + shift) % 26 + 65) if char != ' ' else ' ' for char in ciphertext)
		print(decrypttext)
def main():
	decrypt(sys.argv[1])

if __name__ == "__main__":
	main()
