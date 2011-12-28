import re, bz2, urllib2 as http
import binascii

body = http.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html').read();
un = re.search(r"un: '(.+)'", body).group(1).decode('string_escape')
pw = re.search(r"pw: '(.+)'", body).group(1).decode('string_escape')

print 'user', bz2.decompress(un)
print 'pass', bz2.decompress(pw)
