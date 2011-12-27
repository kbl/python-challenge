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
        return chr(ord(char) + 2)

    return char

print join(map(next_char, text), '')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
