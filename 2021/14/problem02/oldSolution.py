# file = 'fileTest'
file = 'file'

def insertRules(chars, rules):
    newChars = chars[0]

    for rule in rules:
        if chars == rule[0]:
            newChars += rule[1]
            break

    return newChars

with open(file) as f:
    lines = f.readlines()

string = lines.pop(0).strip()
lines.pop(0)

insRules = []
for line in lines:
    l = line.strip().split(" -> ")
    insRules.append(l)

letters = set()
for c in string:
    letters.add(c)
for rule in insRules:
    letters.add(rule[1])

for j in range(10):
    newString = ''
    for i in range(len(string)-1):
        chars = string[i:i+2]
        newString += insertRules(chars, insRules)
    newString += string[len(string)-1]
    string = newString

count = []
for letter in letters:
    count.append(string.count(letter))
count.sort()

print(count[len(count)-1] - count[0])
