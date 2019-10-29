#!/usr/bin/python3

##
## EPITECH PROJECT, 2019
## aes
## File description:
## aes
##

import sys
import string

def check_file(file):
    try:
        open(file, "r")
        return True
    except IOError:
        return False

def check_hexa(value):
    for letters in value:
        if letters not in string.hexdigits and letters is not '\n':
            return False
    return True

def check_args():
    lines = []
    if len(sys.argv) is not 2 or check_file(sys.argv[1]) is not True:
        print("Error: Please enter valid file")
        exit(84)
    file = open(sys.argv[1], "r")
    content = file.readlines()
    lines = content
    if len(lines) is 0 or check_hexa(lines[0]) is not True:
        print("Error: Please enter valid file")
        exit(84)
    if (len(lines[0]) - 1) % 2 is not 0:
        print("Error: Please enter valid key")
        exit(84)
    file.close()
    return lines

def main():
    lines = check_args()
    print(lines)

if __name__ == "__main__":
    main()