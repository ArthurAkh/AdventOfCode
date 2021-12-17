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

maximumHorizontal+=1
maximumVertical+=1

gridMap = [0] * maximumHorizontal
for i in range(maximumHorizontal):
    gridMap[i] = [0] * maximumVertical

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
            if gridMap[x1][i] == 1:
                counter+=1
            gridMap[x1][i]+=1
            i+=1


    elif (y1 == y2):
        minimum = min(x1,x2)
        if(minimum == x1):
            i = x1
            maximum = x2
        else:
            i = x2
            maximum = x1

        while(i <= maximum):
            if gridMap[i][y1] == 1:
                counter+=1
            gridMap[i][y1]+=1
            i+=1


    elif (abs(x2-x1)== abs(y2-y1)):
        minX = min(x1,x2)
        if (minX == x1):
            maxX = x2
            minY = y1
            maxY = y2
        else:
            maxX = x1
            minY = y2
            maxY = y1

        if (minY < maxY):
            yOffset = 1
        else:
            yOffset = -1

        while(minX <= maxX):
            if gridMap[minX][minY] == 1:
                counter+=1
            gridMap[minX][minY]+=1
            minX += 1
            minY += yOffset

# printGrid(gridMap)

print(counter)
