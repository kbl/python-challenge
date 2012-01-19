import Image

picture = Image.open('challenge_11.jpg')
x = picture.convert('CMYK')

x.load()
result1, result2, result3, result4 = x.split()

result1.save('challenge_11_result_1.jpg')
result2.save('challenge_11_result_2.jpg')
result3.save('challenge_11_result_3.jpg')
result4.save('challenge_11_result_4.jpg')
