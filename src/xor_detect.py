#!/usr/bin/python3

import sys
import os
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

def xorDetect(byteArray):
    characterFrequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    line, keyValue = max(((line, key) for line in range(len(byteArray)) for key in range(256)), key = lambda byte:
        sum(characterFrequencies[count] for count in map(lambda count:
            chr(count ^ byte[1]), byteArray[byte[0]]) if count in characterFrequencies))
    keyValue = bytes([keyValue]).hex()
    line = str(line + 1)
    string = (line + " " + keyValue)
    sys.stdout.write(string.upper())

def main():
    argsValidation()
    file = open(sys.argv[1], "r")
    if os.stat(sys.argv[1]).st_size == 0:
        sys.stderr.write("Error: File is empty")
        exit(84)
    fileContent = file.readlines()
    for line in fileContent:
        hexValidation(line)
    file.close()
    data = [bytes.fromhex(re.sub(r'\s', '', num)) for num in fileContent]
    xorDetect(data)
    exit(0)

if __name__ == "__main__":
    main()