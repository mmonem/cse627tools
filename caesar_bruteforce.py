#!/usr/bin/env python

"""
    Caesar Cipher Brute force Decryption
    Author: Mohamed Abdel-Monem Hussein
    E-Mail: mmonem@gmail.com
    Created: 2017-03-16
    Python: 2.7
    License: MIT
"""

import sys

def usage():
    print "Usage: caesar_bruteforce <CIPHERTEXT>"

def caesar_bruteforce(ciphertext):
    for key in range(1,25):
        decrypted = decrypt_caesar(key, ciphertext)
        print "Key: " + str(key) + " " + decrypted

def decrypt_caesar(key, ciphertext):
    ret = ""
    for c in ciphertext:
        d = chr((ord(c) + key) % 26 + ord('A'))
        d = str(d)
        ret += d
    return ret


if len(sys.argv) != 2:
    usage()
    exit(-1)

ciphertext = sys.argv[1]
caesar_bruteforce(ciphertext)
