#!/usr/bin/python3
import sys
import codecs
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
    if len(sys.argv) is not 2 or check_file(sys.argv[1]) is not True:
        print("Error: Please enter valid file")
        exit(84)
    file = open(sys.argv[1], "r")
    readed = file.read()
    if check_hexa(readed) is not True:
        print("Error: invalid file")
        exit(84)
    readed = readed.replace('\n', '')
    if len(readed) % 2 is not 0 or len(readed) is 0:
        print("Error: Invalid hexa")
        exit(84)
    decoded = codecs.encode(codecs.decode(readed, 'hex'), 'base64').decode()
    decoded = decoded.replace('\n', '')
    file.close()
    return decoded

def main():
    new = check_args()
    print(new)

if __name__ == "__main__":
    main()