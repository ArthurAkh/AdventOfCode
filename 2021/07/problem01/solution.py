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

maximum = max(numbers)
minimum = min(numbers)
print(maximum)
print(minimum)


positions = (maximum - minimum) * [0]

for pos in range(len(positions)):
    for i in range (len(numbers)):
        positions[pos] += abs(numbers[i]-(pos+minimum))

minFuel = min(positions)

print(minFuel)
