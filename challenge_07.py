import Image, re

img = Image.open('challenge_07.png')
band = img.crop((0, 43, 608, 44))

letters = []

for x in range(0, 608, 7):
        (r, g, b, a) = band.getpixel((x, 0))
        letters.append(chr(r))

sentence = ''.join(letters)
print sentence 

numbers = re.search('^.+\[(.+)\]$', sentence).group(1).split(',')
letters = [chr(int(n.strip())) for n in numbers]
sentence = ''.join(letters)
print sentence
