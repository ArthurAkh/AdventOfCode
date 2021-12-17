import math

# file = 'fileTest'
file = 'file'

def recursion(inst, num0, num1):
    if len(inst) == 0:
        # print(num0, num1)
        return num0
    i = inst[:1]

    mid = math.ceil((num1 - num0) / 2)
    if i == 'F' or i == 'L':
        num1 = num0 + mid-1
    elif i == 'B' or i == 'R':
        num0 += mid

    # print(i, num0, num1, "mid was", mid)
    return recursion(inst[1:], num0, num1)

def calculate(instRow, instCol):
    row = recursion(instRow, 0, 127)
    col = recursion(instCol, 0, 7)

    # print()
    # print(row, col)
    # exit()
    ans = row * 8 + col

    return ans

with open(file) as f:
    lines = f.readlines()

ids = []
for l in lines:
    l = l.strip()
    row = l[:7]
    col = l[7:]
    ids.append(calculate(row,col))
ids.sort()
for i in range(len(ids)):
    currentS = ids[i]
    nextS = ids[i+1]
    if currentS == nextS - 2:
        print(currentS+1)
        break
# print(max(ids))
# print(ids)
