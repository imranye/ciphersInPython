import math
import random

def encrypt(key, message):
    ciphertext = [''] * key
    for x in range(key):
        pointer = x

        while pointer < len(message):
            ciphertext[x] += message[pointer]
            pointer += key
    return ''.join(ciphertext)


def main():
    message = raw_input('enter a message: ')
    key = int(raw_input('select a key'))
    print(encrypt(key, message))


if __name__ == '__main__':
    main()