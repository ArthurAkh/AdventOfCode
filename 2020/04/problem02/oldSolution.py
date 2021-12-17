# file = 'fileTest'
file = 'file'

with open(file) as f:
    lines = f.readlines()

grid = []
length = len(lines[0].strip())
for line in lines:
    boolLine = length * [0]
    stripped = line.strip()
    for i in range(length):
        c = stripped[i]
        if c == "#":
            boolLine[i] = 1
    grid.append(boolLine)

slope = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
# print(length)
mul = 1

for slop in slope:
    right = slop[0]
    down = slop[1]

    i = 0
    counter = 0

    while((down * i) < len(grid)):
        # print((right * i)%length)
        if(grid[down * i][(right * i)%length] == 1):
            # print(str(down * i) + " " + str((right * i)%length))
            counter+=1
        i+=1
    mul *= counter

print(mul)
