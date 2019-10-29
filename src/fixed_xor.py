#!/usr/bin/python3

#
## EPITECH PROJECT, 2019
## SEC_crypto_2019
## File description:
## challenge02
##

import sys
import string

def check_hexa(value):
    for letters in value:
        if letters not in string.hexdigits and letters is not '\n':
            return False
    return True

def check_file(file):
    try:
        open(file, "r")
        return True
    except IOError:
        return False

def check_args():
    lines = []
    if len(sys.argv) is not 2 or check_file(sys.argv[1]) is not True:
        print("Error: Please enter valid file")
        exit(84)
    file = open(sys.argv[1], "r")
    content = file.readlines()
    lines = content
    file.close()
    if len(lines) is not 2:
        print("Error: Invalid file")
        exit(84)
    lines[0] = lines[0].replace('\n', '')
    lines[1] = lines[1].replace('\n', '')
    if len(lines[0]) is not len(lines[1]) or check_hexa(lines[0]) is not True or check_hexa(lines[1]) is not True:
        print("Error: Invalid file")
        exit(84)
    if len(lines[0]) % 2 is not 0:
        print("Error: Invalid file")
        exit(84)
    return lines

def main():
    lines = check_args()
    print(hex(int(lines[0], 16) ^ int(lines[1], 16)).replace('0x', '').upper())
    return

if __name__ == '__main__':
    main()
    