#!/usr/bin/python3

import base64
import sys
import urllib.request
import urllib.error

cookies = {}

def argsValidation():
    if len(sys.argv) != 1:
        sys.stderr.write("Error: Invalid File or Arguments")
        exit(84)

def request(data):
    request = urllib.request.Request('http://127.0.0.1:5000/challenge10',
        method='POST', data=data,
        headers={'Content-Type': 'text/plain'})
    if cookies:
        request.add_header('Cookie', '; '.join(key+'='+cookies[key] for key in cookies))
    try:
        response = urllib.request.urlopen(request)
        if response.status != 200:
            sys.stderr.write('Server responded with code ' + response.status)
            exit(84)
        for header in response.getheaders():
            if header[0] == 'Set-Cookie':
                cookie = header[1].split('; ')[0].split('=', 1)
                cookies[cookie[0]] = cookie[1]
        return response
    except urllib.error.URLError as error:
        sys.stderr.write('Connection error: ' + repr(error))
        exit(84)

def main():
    argsValidation()
    secret_string1 = base64.b64decode(request(base64.b64encode(b'')).read())
    if len(secret_string1) == 0:
        sys.stderr.write("Secret String is empty")
        exit(84)
    secret_string2 = base64.b64decode(request(base64.b64encode(b'')).read())
    if secret_string1 != secret_string2:
        sys.stderr.write("Failed to get session cookie")
        exit(84)
    index = 0
    while len(secret_string1) == len(secret_string2):
        index += 1
        secret_string2 = base64.b64decode(request(base64.b64encode(bytes(index))).read())
    secret_string3 = secret_string2
    index_copy = index
    while len(secret_string2) == len(secret_string3):
        index_copy += 1
        secret_string3 = base64.b64decode(request(base64.b64encode(bytes(index_copy))).read())
    if index_copy - index != 16:
        sys.stderr.write('Invalid blocksize')
        exit(84)
    secret_string2 = base64.b64decode(request(base64.b64encode(bytes(32))).read())
    if secret_string2[0:16] != secret_string2[16:32]:
        sys.stderr.write('Invalid cipher')
        exit(84)
    full_length = len(secret_string1)
    secret_length = full_length - index

    def decrypt(index, secret):
        if index == secret_length:
            a = full_length - secret_length
            if base64.b64decode(request(base64.b64encode(secret + bytes(a for i in range(a)))).read())[:full_length] == secret_string1:
                return secret
            return

        base = bytes(full_length - index - 1)
        unknown = base64.b64decode(request(base64.b64encode(base)).read())[full_length - 1]
        for index_copy in range(256):
            secret_string3 = bytes([index_copy])
            if unknown == base64.b64decode(request(base64.b64encode(base + secret + secret_string3)).read())[full_length - 1]:
                result = decrypt(index + 1, secret + secret_string3)
                if result:
                    return result

    secret = decrypt(0, bytes())
    sys.stdout.write(base64.b64encode(secret).decode() + '\n')
    exit(0)


if __name__ == "__main__":
    main()