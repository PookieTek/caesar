#!/usr/bin/python3

import sys
import codecs
import string

def fileValidation(file):
    try:
        open(file, "r")
        return True
    except IOError:
        return False


def argsValidation():
    if len(sys.argv) != 2 or fileValidation(sys.argv[1]) is False:
        sys.stderr.write("Error: Invalid File or Arguments")
        exit(84)


def padder(data, size, byte):
    for i in range(0, size):
        if i >= len(data):
            data.append(byte)
    return (data)


def un_padder(data, byte):
    for i in range(0, len(data)):
        if data[i] == byte:
            return (data[:i])

def main():
    argsValidation()
    file = open(sys.argv[1], "r")
    read = file.read()
    read = read.replace('\n', '')
    byte = padder(bytearray("Rijndael", 'utf-8'), 10, 0x02)
    print(byte)
    print(un_padder(byte, 0x02))
    exit(0)


if __name__ == "__main__":
    main()
