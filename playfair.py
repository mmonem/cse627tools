#!/usr/bin/env python

"""
    Caesar Cipher Brute force Decryption
    Author: Mohamed Abdel-Monem Hussein
    E-Mail: mmonem@gmail.com
    Created: 2017-03-17
    Python: 2.7
    License: MIT
"""

import sys

def usage():
    print "Usage: playfair < e | d > <KEY> <PLAINTEXT>"

def prepare_matrix(key):
    return

def prepare_plaintext(plaintext):
    legi = ""

    # Convert to uppercase and ignore non alphabets
    for c in plaintext:
        if ord('A') <= ord(c) <= ord('Z'):
            legi += c
        elif ord('a') <= ord(c) <= ord('z'):
            legi += chr(ord(c) - ord('a') + ord('A'))

    ret = ""
    legi_len = len(legi)
    for i in range(legi_len - 1):
        c1 = legi[i:1]
        ret += c1
        c2 = legi[i+1:1]
        if (c1 == c2):
            ret + 'X'
    return ret

def playfair_encrypt(key, plaintext):
    plaintext = prepare_plaintext(plaintext)
    print plaintext
    ret = ""
    matrix = prepare_matrix(key)
#    for key in range(1,25):
#        decrypted = decrypt_caesar(key, ciphertext)
#        print "Key: " + str(key) + " " + decrypted
    return ret

def playfair_decrypt(key, ciphertext):
    ret = ""
#    for c in ciphertext:
#        d = chr((ord(c) + key) % 26 + ord('A'))
#        d = str(d)
#        ret += d
    return ret


if len(sys.argv) != 4:
    usage()
    exit(-1)

operation = sys.argv[1]
key = sys.argv[2]

if operation == "e":
    plaintext = sys.argv[3]
    ciphertext = playfair_encrypt(key, plaintext)
    print ciphertext
elif operation == "d":
    ciphertext = sys.argv[3]
    plaintext = playfair_decrypt(key, ciphertext)
    print plaintext
else:
    usage()
    exit(-2)

