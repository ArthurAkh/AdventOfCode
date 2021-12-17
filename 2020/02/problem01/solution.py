# file = 'fileTest'
file = 'file'

with open(file) as f:
    lines = f.readlines()

numbers = []
for line in lines:
    firstNum = int(line[:line.find("-")])
    secondNum = int(line[line.find("-")+1:line.find(" ")])
    char = line[line.find(" ")+1:line.find(":")]
    string = line[line.find(":")+2:].strip()
    numbers.append([firstNum, secondNum, char, string])

counter = 0
for line in numbers:
    f = line[0]
    s = line[1]
    c = line[2]
    string = line[3]
    num = string.count(c)
    if (num >= f and num <= s):
        counter+=1

print(counter)
