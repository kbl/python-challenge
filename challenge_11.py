import Image

picture = Image.open('challenge_11.jpg')

picture.load()
result1, result2, result3 = picture.split()

result1.save('challenge_11_result_1.jpg')
result2.save('challenge_11_result_2.jpg')
result3.save('challenge_11_result_3.jpg')
