import Image, re

picture = Image.open('challenge_12.jpg')
length, height = picture.size

new_image = []

def save_image(data, name):
    # image = Image.new('RGB', picture.size)
    # image.putdata(data)
    image = Image.fromstring('RGB', (640, 480), data)
    image.save(name)


for x in xrange(length):
    for y in xrange(height):
        pixel = picture.getpixel((x, y))
        try:
            row = new_image[y]
        except IndexError:
            row = []
            new_image.append(row)
        row.append(pixel)

print len(new_image)
print len(new_image[0])

save_image(new_image, 'test.jpg')

