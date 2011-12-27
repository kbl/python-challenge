import re, zipfile

nothing = '90052'
stack = []
zip = zipfile.ZipFile('challenge_06.zip')

while True:
    stack.append(nothing)

    zipped_file = zip.open(nothing + '.txt')
    body = zipped_file.read()
    # print body
    matched = re.search(r'nothing is (\d+)', body)
    if matched:
        nothing = matched.group(1)
    else:
        break

x = ''
for number in stack:
    x += zip.getinfo(number + '.txt').comment

zip.close()

print x
