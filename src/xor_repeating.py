#!/usr/bin/python3

import sys
import os
import re
import string
import itertools
import codecs

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

def xorRepeating(message, key):
    #index, output = 0, b''
    #for byte in message:
    #    output += bytearray([int(byte, 16) ^ int(key[index], 16)])
    #    index += (index < len(key) - 1) if 1 else 0
    #string = output.hex().replace('00', 'O').replace('01', '1').replace('02', '2').replace('03', '3').replace('04', '4').replace('05', '5').replace('06', '6').replace('07', '7').replace('08', '8').replace('09', '9').replace('0a', 'a').replace('0b', 'b').replace('0c', 'c').replace('0d', 'd').replace('0e', 'e').replace('0f', 'f').replace('O', '0')
    
    string = bytearray(messageChr ^ keyChrCycle for messageChr, keyChrCycle in zip(message, itertools.cycle(key)))
    sys.stdout.write(string.hex().upper() + '\n')

def main():
    argsValidation()
    if os.stat(sys.argv[1]).st_size == 0:
        sys.stderr.write("Error: File is empty")
        exit(84)
    file = open(sys.argv[1], "r")
    fileContent = file.readlines()
    file.close()
    for line in fileContent:
        hexValidation(line)
    key = re.sub(r'\s', "", fileContent[0])
    try:
        message = re.sub(r'\s', "", fileContent[1])
    except IndexError:
        sys.stderr.write('Error: Message doesn\'t exist')
        exit(84)
    xorRepeating(codecs.decode(message, "hex"), codecs.decode(key, "hex"))
    exit(0)

if __name__ == "__main__":
    main()
