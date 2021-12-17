import math

# file = 'fileTest'
file = 'file'

def printG (grid):
    for line in grid:
        toPrint = []
        for x in range(len(grid[0])):
            if line[x]:
                c = '#'
            else:
                c = ' '
            toPrint.append(c)
        print(''.join(toPrint))

def fold (grid, d, half):
    new = []
    if d == "x":
        # print("half x", half)
        for i in range(len(grid)):
            temp = (half) * [False]
            new.append(temp)
        for y in range(len(new)):
            for x in range(len(new[0])):
                new[y][x] = grid[y][x] or grid[y][2*half - x]


    elif d == "y":
        # print("half y", half)
        for i in range(half):
            temp = (len(grid[0])) * [False]
            new.append(temp)
        for y in range(len(new)):
            for x in range(len(new[0])):
                new[y][x] = grid[y][x] or grid[2*half - y][x]


    return new


with open(file) as f:
    lines = f.readlines()

listDots = []
for line in lines:
    l = line.strip().split(",")
    if l == ['']:
        break
    l = list(map(int, l))
    listDots.append(l)

instructions = []
for i in range(len(lines)-1, -1, -1):
    l = lines[i].split(' ')
    if l == ['\n']:
        break
    inst = l[2].strip()
    inst = inst.split("=")
    inst[1] = int(inst[1])
    instructions.append(inst)

maxX = -99999
maxY = -99999
for c in listDots:
    x = c[0]
    maxX = max(maxX, x)
    y = c[1]
    maxY = max(maxY, y)

maxX+=1
maxY+=1

grid = []
for i in range(maxY):
    temp = maxX * [False]
    grid.append(temp)

for l in listDots:
    x = l[0]
    y = l[1]
    grid[y][x] = True

instructions.reverse()
# print(grid)
for inst in instructions:
    grid = fold(grid, inst[0], inst[1])
printG(grid)
