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

counter = 0
i = 0
right = 3
down = 1
# print(length)

while((down * i) < len(grid)):
    # print((right * i)%length)
    if(grid[down * i][(right * i)%length] == 1):

        print(str(down * i) + " " + str((right * i)%length))
        counter+=1
    i+=1
print(counter)
