# multi-line statement
''' This program returns the occurance of a value in the sequence '''

def count(sequence, item):
    ''' This function returns the occurance of a value in the sequence'''
    y = 0
    for n in sequence:
        if n == item:
            y += 1

    return y
