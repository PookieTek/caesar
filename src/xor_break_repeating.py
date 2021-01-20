#!/usr/bin/python3

import sys
import os
import re
import string

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

def average(list):
    return sum(list) / len(list)

def stepZip(list, step):
    return zip(*(list[i::step] for i in range(step)))

def breakKey(data):
    characterFrequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    keySizes = sorted(range(1, 41), key=lambda k: average([sum(bin(a ^ b).count('1') for a, b in zip(a, b)) / k for a, b in stepZip([data[i:i+k] for i in range(0, len(data), k)], 2)]))[:5]
    for size in keySizes:
        scoreList = []
        key = bytes(max(range(256), key=lambda k: sum(characterFrequencies[b] for b in map(lambda b: chr(b ^ k), data[i::size]) if b in characterFrequencies)) for i in range(size))
        score = sum(characterFrequencies[b] for b in map(lambda k: chr(k[1] ^ key[k[0] % len(key)]), enumerate(data)) if b in characterFrequencies)
        scoreList.append((key, score))
    key = sorted(scoreList, key=lambda k: (k[1], 1 / len(k[0])))[-1][0]
    sys.stdout.write(key.hex().upper() + '\n')

def main():
    argsValidation()
    if os.stat(sys.argv[1]).st_size == 0:
        sys.stderr.write("Error: File is empty")
        exit(84)
    file = open(sys.argv[1], "r")
    try:
        data = bytes.fromhex(re.sub(r'\s', '', file.read()))
    except ValueError:
        sys.stderr.write("Error: Non-Hexadecimal digit found")
        exit(84)
    file.close()
    breakKey(data)
    exit(0)


if __name__ == "__main__":
    main()