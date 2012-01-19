import Image, re

picture = Image.open('challenge_11.jpg')
length, height = picture.size
new_size = (length / 2, height / 2)

odd_odd = []
odd_even = []
even_odd = []
even_even = []

def even(x):
    return x % 2 == 0 and 'even' or 'odd'

def save_image(data, name):
    image = Image.new('RGB', new_size)
    image.putdata(data)
    image.save(name)

for x in xrange(length):
    for y in xrange(height):
        where = '%s_%s' % (even(x), even(y))
        locals()[where].append(picture.getpixel((x, y)))

for name in ['odd_odd', 'odd_even', 'even_odd', 'even_even']:
    save_image(locals()[name], name + '.jpg')

