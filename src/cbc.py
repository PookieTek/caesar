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


def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


def unpad(s):
    return s[:-ord(s[len(s)-1:])]


def main():
    argsValidation()
    file = open(sys.argv[1], "r")
    Lines = file.readlines()
    if len(Lines) != 3 or len((Lines[2])[:-1]) % 16 != 0 or len((Lines[0])[:-1]) % 16 != 0 or len((Lines[1])[:-1]) % 16 != 0:
        exit(84)
    hex_key = bytes.fromhex((Lines[0])[:-1])
    iv = bytes.fromhex((Lines[1])[:-1])
    key = hex_key.decode("ASCII")
    cipher = AES.new(key, AES.MODE_ECB)
    to_decrypt = base64.b64decode((Lines[2])[:-1])
    block_size = 16
    str = b""
    chunks = [to_decrypt[i:i+block_size] for i in range(0, len(to_decrypt), block_size)]
    temp = iv
    for i in range(0, len(chunks)):
        if (len(chunks[i]) % 16 != 0):
            break
        temp2 = chunks[i]
        chunks[i] = cipher.decrypt(chunks[i])
        chunks[i] = byte_xor(chunks[i], temp)
        str += chunks[i]
        temp = temp2
    str = base64.b64encode(str)
    sys.stdout.write(str.decode() + '\n')
    exit(0)


if __name__ == "__main__":
    main()
