# file = 'fileTest'
file = 'file'

def augmentNeighbors(i, j, n, b):
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not(x == 0 and y == 0):
                if i+x >= 0 and i+x < len(n) and j+y >= 0 and j+y < len(n[0]):
                    if b[i+x][j+y] == False:
                        n[i+x][j+y] += 1

def flash(n, b, q, nmb):
    for i in range(len(n)):
        for j in range(len(n[0])):
            if n[i][j] > 9:
                nmb+=1
                n[i][j] = 0
                b[i][j] = True
                q.append([i,j])
    return nmb

def reset(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            b[i][j] = False

def processFlashes(n, b, q):
    for cell in q:
        i = cell[0]
        j = cell[1]
        augmentNeighbors(i, j, n, b)

def energyOne(n):
    for i in range(len(n)):
        for j in range(len(n[0])):
            n[i][j]+=1

with open(file) as f:
    lines = f.readlines()

grid = []
for line in lines:
    l = line.strip()
    newLine = []
    for c in l:
        newLine.append(int(c))
    grid.append(newLine)

b = []
for i in range(len(grid)):
    temp = len(grid[0]) * [False]
    b.append(temp)

q = []
nmb = 0
for i in range(100):
    energyOne(grid)
    while(1):
        nmb = flash(grid, b, q, nmb)
        if len(q)==0:
            break
        processFlashes(grid, b, q)
        q = []
    reset(b)
print(nmb)
