#!/usr/bin/python3

import sys
import re
import string

def hexValidation(hexstring):
    for i in hexstring:
        if i not in string.hexdigits and i != '\n':
            sys.stderr.write("Error: Non-Hexadecimal digit found")
            exit(84)

def fileValidation(file):
    try:
        open(file, "r")
        return True
    except IOError:
        return False

def argsValidation():
    if len(sys.argv) != 2 or fileValidation(sys.argv[1]) == False:
        sys.stderr.write("Error: Invalid File or Arguments")
        exit(84)

def keyValue(byteArray):
    characterFrequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    keyValue = max(range(256), key = lambda byte:
        sum(characterFrequencies[count] for count in map(lambda count:
            chr(count ^ byte), byteArray) if count in characterFrequencies))
    string = bytes([keyValue]).hex()
    sys.stdout.write(string.upper() + '\n')

def main():
    argsValidation()
    file = open(sys.argv[1], "r")
    read = file.read()
    read = read.replace('\n', '')
    file.close()
    hexValidation(read)
    if len(read) % 2 != 0 or len(read) == 0:
        sys.stderr.write("Error: Hexadecimal value is invalid")
        exit(84)
    keyValue(bytearray.fromhex(read))
    exit(0)

if __name__ == "__main__":
    main()
