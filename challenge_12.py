import Image, re

picture = Image.open('challenge_12.jpg')
length, height = picture.size

new_image = []

modified = picture.transform(picture.size, 
                             Image.AFFINE, 
                             (1, 0, 0, 0, 1, -3))
modified.show()

