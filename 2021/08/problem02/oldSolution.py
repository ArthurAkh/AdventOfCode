# file = 'fileTest'
file = 'file'

with open(file) as f:
    lines = f.readlines()

listABC = []
for line in lines:
    strings = (line[:line.find("|")-1]).split(" ")
    digits = line[line.find("|")+1:].strip().split(" ")
    listABC.append([strings,digits])

easyDigits = [2, 4, 3, 7]

counter = 0
for line in listABC:
    digits = line[1]

    for digit in digits:
        length = len(digit)
        for d in easyDigits:
            if length == d:
                counter+=1

print(counter)
