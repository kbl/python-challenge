# a  = [1, 11, 21, 1211, 111221, 
#       1   4   7  49    376
# len(a[30]) = ?

def convert(number):
    base = 3
    exponent = 0
    value = 0
    for char in str(number)[::-1]:
        value += base ** exponent * int(char)
        print base, exponent, int(char), value
        exponent += 1

    return value

print '111221 = ', convert('111221')
