#!/usr/bin/python3

##
## EPITECH PROJECT, 2019
## xor
## File description:
## xor
##

import sys

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
    if len(lines) is 0:
        print("Error: Please enter valid file")
        exit(84)
    file.close()
    return lines

def main():
    lines = check_args()
    print(lines)

if __name__ == "__main__":
    main()