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


def count_repetition(ciphertext, block_size):
    chunks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
    number_of_repetitions = len(chunks) - len(set(chunks))
    result = {
        "ciphertext": ciphertext,
        "repetitions": number_of_repetitions
    }
    return (result)


def main():
    argsValidation()
    file = open(sys.argv[1], "r")
    Lines = file.readlines()
    for i in range(0, len(Lines)):
        Lines[i] = base64.b64decode((Lines[i])[:-1])
        if len(Lines[i]) % 16 != 0:
            exit(84)
    repetitions = [count_repetition(cipher, 16) for cipher in Lines]
    most_repetitions = sorted(repetitions, key=lambda x: x['repetitions'], reverse=True)[0]
    for i in range(0, len(Lines)):
        if Lines[i] == most_repetitions['ciphertext']:
            print (i+1)
            break
    exit(0)


if __name__ == "__main__":
    main()
