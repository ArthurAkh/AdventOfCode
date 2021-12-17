# file = 'fileTest'
file = 'file'

with open(file) as f:
    lines = f.readlines()

numbers = []
for line in lines:
    numbers.append(int(line.strip()))

for i in range(len(numbers)):
    for j in range(len(numbers)):
        temp = numbers[i] + numbers[j]
        if temp == 2020:
            print(str(numbers[i] * numbers[j]))
            exit()
