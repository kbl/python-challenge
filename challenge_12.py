from itertools import cycle

files = [open('result_%s.jpg' % str(i + 1), 'w') for i in xrange(5)]
index = cycle(range(5))

with open('challenge_12.gfx') as f:
    for x in f:
        files[index.next()].write(x)

for f in files:
    f.close()
