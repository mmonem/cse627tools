#!/usr/bin/env python

"""
    Hill Cipher Encryption
    Author: Mohamed Abdel-Monem Hussein
    E-Mail: mmonem@gmail.com
    Created: 2017-03-17
    Python: 2.7
    License: MIT
"""

import sys

def usage():
    print "Usage: hill_encrypt <k11> <k12> <k21> <k22>  <QUOTED PLAINTEXT>"

def prepare_plaintext(plaintext):
    legi = ""

    # Convert to uppercase and ignore non alphabets
    for c in plaintext:
        if ord('A') <= ord(c) <= ord('Z'):
            legi += c
        elif ord('a') <= ord(c) <= ord('z'):
            legi += chr(ord(c) - ord('a') + ord('A'))
    if len(legi) % 2 != 0:
        legi += "X"
    return legi

def hill_encrypt(k11, k12, k21, k22, plaintext):
    ciphertext = ""
    plaintext = prepare_plaintext(plaintext)
    rounds = len(plaintext) / 2
    for r in range(rounds):
        p1 = ord(plaintext[r * 2]) - ord('A')
        p2 = ord(plaintext[r * 2 + 1]) - ord('A')
        c1 = chr((k11 * p1 + k12 * p2) % 26 + ord('A'))
        c2 = chr((k21 * p1 + k22 * p2) % 26 + ord('A'))
        ciphertext += c1
        ciphertext += c2
    return ciphertext

if len(sys.argv) != 6:
    usage()
    exit(-1)

operation = sys.argv[1]
key = sys.argv[2]

k11 = int(sys.argv[1])
k12 = int(sys.argv[2])
k21 = int(sys.argv[3])
k22 = int(sys.argv[4])
plaintext = sys.argv[5]
ciphertext = hill_encrypt(k11, k12, k21, k22, plaintext)
print ciphertext
