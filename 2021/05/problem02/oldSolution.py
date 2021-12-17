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

clean01 = []
for line in lines:
    clean01.append(line.strip())


clean02 = []
for line in clean01:
    clean02.append(line.split(' -> '))

clean03 = []
for inside in clean02:
    for line in inside:
        clean03.append(line.split(','))

ventsList = []
for i in range(len(clean03)):
    if(i%2 == 0):
        line1 = clean03[i]
        line2 = clean03[i+1]
        ventsList.append([int(line1[0]),int(line1[1]),int(line2[0]),int(line2[1])])

# print(ventsList)

# find largest number
maximumHorizontal = 0
maximumVertical = 0

for line in ventsList:
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]
    maxH = max(x1, x2)
    maxV = max(y1, y2)
    maximumHorizontal = max(maximumHorizontal, maxH)
    maximumVertical = max(maximumVertical, maxV)

maximumHorizontal+=2

# print(maximumHorizontal)
# print(maximumVertical)

gridMap = [0] * maximumVertical
for i in range(maximumVertical):
    gridMap[i] = [0] * maximumHorizontal

# add the lines from ventsList to gridMap
counter = 0
for line in ventsList:
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]
    # print("Working on this")
    # print(line)

    if(x1 == x2):
        minimum = min(y1,y2)
        if(minimum == y1):
            i = y1
            maximum = y2
        else:
            i = y2
            maximum = y1

        while(i <= maximum):
            # print(line)
            # print("added " + str(x1) + " and " + str(i))
            if gridMap[x1][i] == 1:
                counter+=1
            gridMap[x1][i]+=1
            i+=1
            # printGrid(gridMap)
            # time.sleep(4)

    elif (y1 == y2):
        minimum = min(x1,x2)
        if(minimum == x1):
            i = x1
            maximum = x2
        else:
            i = x2
            maximum = x1

        while(i <= maximum):
            # print(line)
            # print("added point at " + str(i) + ", " + str(y1))
            if gridMap[i][y1] == 1:
                counter+=1
            gridMap[i][y1]+=1
            i+=1
            # printGrid(gridMap)
            # time.sleep(4)
    # else:
        # print("this was a diagonal")
        # print()

# printGrid(gridMap)

print(counter)

exit()

string_numbers = lines[0]
random_numbers = []

strippedNumbers = string_numbers.split(",")
# print(strippedNumbers)
for string in strippedNumbers:
    random_numbers.append(int(string))


lines.pop(0)
lines.pop(0)

grid = []
grids = []
j = 0

for i in range(len(lines)):
    # print(lines[i])
    if(len(lines[i]) > 1):
        # print(lines[i])
        strippedString = lines[i].strip()
        # print(strippedString)
        strippedList = list(strippedString.split(" "))
        digits = []
        # print(strippedList)
        for string in strippedList:
            if(string != ''):
                digits.append(int(string))

        # print(digits)
        # print("now, new one")
        # print("")

        grid.append(digits)

    if(j == 4):
        j = -1
        grids.append(grid)
        grid = []
    else:
        j+=1

# for grid in grids:
#     print(grid)

# print(grids[0])
# print(grids[1])
# print(grids[2])
# print(grids[3])

# print (grids)

# print(random_numbers)


f.close()
# exit()


memo = {}
for num in random_numbers:
    memo[num] = []
for gi, grid in enumerate(grids):
    for ri, row in enumerate(grid):
        for ci, num in enumerate(row):
            if num in memo:
                memo[num].append((gi, ri, ci))

def is_win(grid, row, col):
    grid[row][col] = -1
    if sum(grid[row]) == -5:
        return True
    if sum([row[col] for row in grid]) == -5:
        return True
    return False

def process_winner(grids, grid_indexes):
    for gi, ri, ci in grid_indexes:
        grid = grids[gi]

        if is_win(grid, ri, ci):

            return sum(
                [(0 if grid[i][j] == -1 else grid[i][j]) for i in range(5) for j in range(5)]
            ) * num

    return None

ans = 0
for num in random_numbers:
    ans = process_winner(grids, memo[num])

    if ans is not None:
        break
print(f'Answer: {ans}')
