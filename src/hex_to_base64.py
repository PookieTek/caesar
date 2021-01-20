#!/usr/bin/python3

import sys
import codecs
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

def main():
    argsValidation()
    file = open(sys.argv[1], "r")
    read = file.read()
    read = read.replace('\n', '')
    hexValidation(read)
    if len(read) % 2 != 0 or len(read) == 0:
        sys.stderr.write("Error: Hexadecimal value is invalid")
        exit(84)
    base64 = codecs.encode(codecs.decode(read, "hex"), "base64").decode()
    file.close()
    sys.stdout.write(base64)
    exit(0)

if __name__ == "__main__":
    main()
