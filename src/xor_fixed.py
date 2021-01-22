#!/usr/bin/python3

import sys
import os
import re
import string

def check_hexa(value):
    for letters in value:
        if letters not in string.hexdigits and letters != '\n':
            return False
    return True

def check_file(file):
    try:
        open(file, "r")
        return True
    except IOError:
        return False

def fileValidation(file):
    try:
        open(file, "r")
        return True
    except IOError:
        return False

def check_args():
    if len(sys.argv) != 2 or fileValidation(sys.argv[1]) is False:
        sys.stderr.write("Error: Invalid File or Arguments")
        exit(84)

def main():
    lines = []
    check_args()
    file = open(sys.argv[1], "r")
    content = file.readlines()
    lines = content
    file.close()
    if len(lines) != 2:
        print("Error: Invalid file")
        exit(84)
    lines[0] = lines[0].replace('\n', '')
    lines[1] = lines[1].replace('\n', '')
    if len(lines[0]) is not len(lines[1]) or check_hexa(lines[0]) is not True or check_hexa(lines[1]) is not True or len(lines[0]) % 2 != 0:
        print("Error: Invalid file")
        exit(84)
    print(hex(int(lines[0], 16) ^ int(lines[1], 16)).replace('0x', '').upper())
    return

if __name__ == '__main__':
    main()
