# file = 'fileTest'
file = 'file'

def check(f):
    if f[0] == "cid":
        return True

    if f[0] == 'byr':
        if int(f[1]) >= 1920 and int(f[1]) <= 2002:
            return True

    elif f[0] == 'iyr':
        if int(f[1]) >= 2010 and int(f[1]) <= 2020:
            return True

    elif f[0] == 'eyr':
        if int(f[1]) >= 2020 and int(f[1]) <= 2030:
            return True

    elif f[0] == 'hgt':
        if f[1][-2:] == 'cm':
            if f[1][:3].isnumeric() and int(f[1][:3]) >= 150 and int(f[1][:3]) <= 193:
                return True
        elif f[1][-2:] == 'in':
            if int(f[1][:2]) >= 59 and int(f[1][:2]) <= 76:
                return True

    elif f[0] == 'hcl':
        if len(f[1]) == 7 and f[1][0] == '#':
            allowedChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
            string = f[1][1:]
            for c in string:
                present = False
                for char in allowedChar:
                    if(c == char):
                        present = True
                if not present:
                    return False
            return True

    elif f[0] == 'ecl':
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        for c in colors:
            if f[1] == c:
                return True

    elif f[0] == 'pid':
        if len(f[1]) == 9:
            return f[1].isnumeric()
    # print("failed", f)

    return False


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
        valid = True
        for field in pas:
            # print(field)
            valid = valid and check(field)

        if valid:
            numValid += 1
print(numValid)
