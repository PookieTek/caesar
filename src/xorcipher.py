#!/usr/bin/python3

##
## EPITECH PROJECT, 2019
## SEC_crypto_2019
## File description:
## challenge03
##

import sys
import re
import string

def check_hexa(value):
    for letters in value:
        if letters not in string.hexdigits:
            return False
    return True

def check_file(file):
    try:
        open(file, "r")
        return True
    except IOError:
        return False

def check_args():
    if len(sys.argv) is not 2 or check_file(sys.argv[1]) is not True:
        print("Error: Please enter valid file")
        exit(84)
    file = open(sys.argv[1], "r")
    decoded = file.read()
    decoded = decoded.replace('\n', '')
    file.close()
    if check_hexa(decoded) is not True:
        print("Error: Invalid file")
        exit(84)
    if len(decoded) is 0:
        print("Error: Invalid hexa")
        exit(84)
    return decoded

def keyvalue(arrayofbyte):
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    keyvalue = max(range(256), key = lambda byte:
        sum(character_frequencies[count] for count in map(lambda count:
            chr(count ^ byte), arrayofbyte) if count in character_frequencies))
    string = bytes([keyvalue]).hex()
    print(string.upper())

def main():
    string = check_args()
    keyvalue(bytearray.fromhex(string))

if __name__ == '__main__':
    main()