#!/usr/bin/python3

import sys
import codecs
import string
import base64
from Crypto.Cipher import AES

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


def unpad(s):
    return s[:-ord(s[len(s)-1:])]


def main():
    argsValidation()
    file = open(sys.argv[1], "r")
    Lines = file.readlines()
    if len(Lines) != 2 or len((Lines[0])[:-1]) % 16 != 0:
        exit(84)
    hex_key = bytes.fromhex((Lines[0])[:-1])
    key = hex_key.decode("ASCII")
    cipher = AES.new(key, AES.MODE_ECB)
    to_decrypt = base64.b64decode((Lines[1])[:-1])
    to_decrypt = cipher.decrypt(to_decrypt)
    to_decrypt = unpad(to_decrypt)
    to_decrypt = base64.b64encode(to_decrypt)
    sys.stdout.write(to_decrypt.decode() + '\n')
    ##print(base64.b64encode(to_decrypt))
    exit(0)


if __name__ == "__main__":
    main()
