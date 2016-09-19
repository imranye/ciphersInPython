#imran muthuvappa
#reverse cipher
#based on http://inventwithpython.com/hacking
#Just doing the excersizes the way I would

def encode(message, x, encoded):
    while x >= 0:
        encoded += message[x]
        x -= 1
    return encoded    


def main():
    message = raw_input('Enter message to be encoded:  ')
    encoded = ''
    x = len(message) - 1
    print('your encoded message is  ' + encode(message, x, encoded))


main()





