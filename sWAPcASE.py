def swapCase(s):
    k =  ' '
    for i in s:
        if i.isupper() == True:
            i = i.lower()
            k += i
        else:
            i = i.upper()
            k += i
    return k

def main():
    s = raw_input('enter a string')
    print(swapCase(s))


main()
