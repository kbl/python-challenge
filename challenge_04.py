import re, urllib2 as http
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=X'

nothing = 44827
nothing = 8022
nothing = 82682

while True:
    response = http.urlopen(url.replace('X', str(nothing))).read()
    print response
    nothing = int(re.search(r'next nothing is (\d+)', response).group(1))
