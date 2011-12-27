import pickle

file = open('pickle_06.txt')
obj = pickle.load(file)
file.close()

for row in obj:
    print "".join(map(lambda (sign, count): sign * count, row))
