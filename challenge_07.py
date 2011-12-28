import Image

img = Image.open('challenge_07.png')
band = img.crop((0, 43, 608, 44))

letters = []

for letter in list(band.getdata()):
    print chr(letter[0])
