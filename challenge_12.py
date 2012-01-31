import Image, re

picture = Image.open('challenge_12.jpg')
length, height = picture.size
new_size = (length / 2, height)

images = {'image1': [], 'image2': []}

def even(x):
    return x % 2 == 0 and 'image1' or 'image2'

def save_image(data, name):
    image = Image.new('RGB', new_size)
    image.putdata(data)
    image.save(name)

for x in xrange(length):
    lines = { 'image1': [], 'image2': [] }
    for y in xrange(height):
        lines[even(x)].append(picture.getpixel((x, y)))
    print len(lines)
    for name, line in lines.values():
        images[name].append(line)

for name, image in images.values():
    save_image(image, name + '.jpg')

