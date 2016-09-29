import math #used for pythons math functions
import random #python random library

def encrypt(key, message):
    #takes in a key and a message, only encrypts
    ciphertext = [''] * key
    for x in range(key):
        pointer = x

        while pointer < len(message):
            ciphertext[x] += message[pointer]
            pointer += key
    return ''.join(ciphertext)


def main():
    #takes user input, prints encrypted result
    message = raw_input('enter a message: ')
    key = int(raw_input('select a key'))
    print(encrypt(key, message))


if __name__ == '__main__':
    main()