import pyperclip

def caesar(message, key, mode):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''
    message = message.upper()
    for i in message:
        num = LETTERS.find(i)
        if mode == 'encrypt' :
            num += key
        elif mode == 'decrypt':
            num-= key
        if num >= len(LETTERS):
            num -= len(LETTERS)
        elif num < 0:
            num += len(LETTERS)
        translated += LETTERS[num]

    else:
        translated += i

    return translated


def main():
    message = raw_input('enter a message:  ')
    key = int(raw_input('select a key value: '))
    mode = raw_input('encrypt or decrypt:  ')
    translated = caesar(message, key, mode)
    print(translated)
    pyperclip.copy(translated)

main()

