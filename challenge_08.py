import re, bz2, urllib2 as http
import binascii

body = http.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html').read();
un = re.search(r"un: '(.+)'", body).group(1)
pw = re.search(r"pw: '(.+)'", body).group(1)

print 'un [[' + un + ']]'
print 'pw [[' + pw + ']]'

def repl(match_data):
    return binascii.unhexlify(match_data.group(1))

pw = re.sub(r'\\x(.{2})', repl, pw)
un = re.sub(r'\\x(.{2})', repl, un)
un = re.sub(r'\\r', chr(13), un)

print 'un [[' + un + ']]'
print 'pw [[' + pw + ']]'

print 'user', bz2.decompress(un)
print 'pass', bz2.decompress(pw)
