#imran muthuvappa
#reverse cipher
#based on http://inventwithpython.com/hacking


def encode(message, x, encoded):
    while x >= 0:
        encoded += message[x]
        x -= 1
    return encoded    


def main():
    message = 'Super secret club meets on wednesday'
    encoded = ''
    x = len(message) - 1
    print(encode(message, x, encoded))


main()





