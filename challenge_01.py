from string import join 
import re

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def next_char(char, step = 2):
    """ counts next letter character

        >>> next_char('a')
        'c'
        >>> next_char('z')
        'b'
        >>> next_char(')')
        ')'
    """
    if re.match('[a-z]', char):
        a = ord('a')
        z = ord('z')
        new_char = ord(char) + 2
        if new_char > z: 
            return chr(new_char % z + a - 1)
        else:
            return chr(new_char)

    return char

print join(map(next_char, text), '')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
