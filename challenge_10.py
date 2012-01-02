#       1  2   2   4     6
# a  = [1, 11, 21, 1211, 111221, 
#       1  4   7   49    376
# len(a[30]) = ?

def encode(value):
    '''
    >>> encode('1211')
    '111221'
    >>> encode('111221')
    '312211'
    '''

    previous = None
    count = 0
    encoded = ''

    def encode_char():
        return str(count) + str(previous)

    for char in value:
        if previous == None:
            count = 1
            previous = char
            continue
        if char == previous:
            count += 1
        else:
            encoded += encode_char()

            count = 1
            previous = char

    encoded += encode_char()
        
    return encoded

a = ['1']

for i in range(30):
    current = a[i]
    a.append(encode(current))

print len(a[30])

# 5808

if __name__ == '__main__':
    import doctest
    doctest.testmod()

