file = 'file'

with open(file) as f:
    lines = f.readlines()

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

f.close()

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


winners = []
def process_winner(grids, grid_indexes):
    for gi, ri, ci in grid_indexes:

        if gi in winners:
            continue

        grid = grids[gi]

        if is_win(grid, ri, ci):
            winners.append(gi)

            if len(winners) == len(grids):
                return sum(
                    [(0 if grid[i][j] == -1 else grid[i][j]) for i in range(5) for j in range(5)]
                ) * num
    return None

ans = None
for num in random_numbers:
    ans = process_winner(grids, memo[num])

    if ans is not None:
        break
print(f'Answer: {ans}')
