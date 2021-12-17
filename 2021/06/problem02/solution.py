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

# fishes in stage 0 1 2 3 4 5 6 7 8
fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for number in numbers:
    fishes[number]+=1

# print(numbers)
# print(fishes)

# simulate 256 days
days = 256

while(days > 0):
    days-=1
    temp = fishes[0]
    for i in range(8):
        fishes[i] = fishes[i+1]
    fishes[6] += temp
    fishes[8] = temp



sum = 0
for fishNum in fishes:
    sum+=fishNum

print(sum)
