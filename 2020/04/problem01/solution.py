# file = 'fileTest'
file = 'file'

with open(file) as f:
    lines = f.readlines()

listP = []
temp = []

for line in lines:
    if line == '\n':
        listP.append(temp)
        temp = []
    else:
        line = line.strip().split(" ")
        for l in line:
            tempField = []

            tempField.append(l[:l.find(":")])
            tempField.append(l[l.find(":")+1:])
            temp.append(tempField)
        if line == lines[len(lines)-1].strip().split(" "):
            listP.append(temp)

possibleFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
numValid = 0
for pas in listP:
    num = 0
    for field in pas:
        for possibleF in possibleFields:
            if field[0] == possibleF:
                num += 1
    if num >= 7:
        numValid += 1
print(numValid)
