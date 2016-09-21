import math

def decrypt(key, message):
    columns = numOfColumns = math.ceil(len(message) / key)
    ShadedBoxes = (numOfColumns * numOfRows) - len(message)
    rows = key
    plaintext = [''] * numOfColumns
    col = 0
    row = 0
    for i in message:
        plaintext[col] += symbol
        col += 1
        if (col == columns) or (col == columns - 1 and row >= rows - ShadedBoxes):
