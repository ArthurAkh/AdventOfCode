import time

# file = 'fileTest'
file = 'file'

def printGrid(grid):
    for i in range(len(grid)):
        toPrint = '.' * len(grid[0])
        for j in range(len(grid[0])):
            num = grid[i][j]
            if num > 0:
                toPrint = toPrint[:j] + str(num) + toPrint[j+1:]
        print(toPrint)

with open(file) as f:
    lines = f.readlines()

numbersStr = lines[0].strip().split(',')

numbers = []
for number in numbersStr:
    numbers.append(int(number))

# simulate 80 days
days = 80
while(days > 0):
    days-=1
    count = 0
    for index in range(len(numbers)):
        if(numbers[index] <= 0):
            numbers[index] = 6
            count+=1
        else:
            numbers[index]-=1

    for i in range(count):
        numbers.append(8)

print(len(numbers))
