import pickle

file = open('pickle_06.txt')
obj = pickle.load(file)
file.close()

for row in obj:
    string = ''
    for (sign, count) in row:
        string += sign * count
    print string
