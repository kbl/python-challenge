import Image

image = Image.open('challenge_11.jpg')
length, width = image.size

result1 = Image.new('L', (length, width))
result2 = Image.new('L', (length, width))
result3 = Image.new('L', (length, width))

for x in xrange(length):
    for y in xrange(width):
        a, b, c = image.getpixel((x, y))
        result1.putpixel((x, y), a)
        result2.putpixel((x, y), b)
        result3.putpixel((x, y), c)

result1.save('challenge_11_result_1.jpg')
result2.save('challenge_11_result_2.jpg')
result3.save('challenge_11_result_3.jpg')
