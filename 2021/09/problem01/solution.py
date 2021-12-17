# file = 'fileTest'
file = 'file'

def checkNeighborBiggerSmaller(i, j, g, dHeight, dWidth, positive):
    ans = g[i+dHeight][j+dWidth] <= g[i][j]
    if (positive):
        return ans
    return not ans


def isSmallest(i, j, g, bGrid):
    if bGrid[i][j] == False:
        return False
    height = len(g)-1
    width = len(g[0])-1
    # if i is 0 or is height
    if (i == 0 or i == height):
        # at most 3 neighbors
        if i == 0:
            ans = checkNeighborBiggerSmaller(i,j,g,1,0,False)
            # print(g[i+1][j])
            # print(ans)
            # print(i)
            # print(j)
            if ans:
                bGrid[i+1][j] = False
            if j == 0:
                ans2 = checkNeighborBiggerSmaller(i,j,g,0,1,False)
                if ans2:
                    bGrid[i][j+1] = False
                return ans and ans2

            elif j == width:
                ans2 = checkNeighborBiggerSmaller(i,j,g,0,-1,False)
                if ans2:
                    bGrid[i][j-1] = False
                return ans and ans2

            else:
                ans2 = checkNeighborBiggerSmaller(i,j,g,0,-1,False)
                if ans2:
                    bGrid[i][j-1] = False
                ans3 = checkNeighborBiggerSmaller(i,j,g,0,1,False)
                if ans3:
                    bGrid[i][j+1] = False
                return ans and ans2 and ans3
        else: # i == height
            ans = checkNeighborBiggerSmaller(i,j,g,-1,0,False)
            if j == 0:
                ans2 = checkNeighborBiggerSmaller(i,j,g,0,1,False)
                if ans2:
                    bGrid[i][j+1] = False
                return ans and ans2

            elif j == width:
                ans2 = checkNeighborBiggerSmaller(i,j,g,0,-1,False)
                if ans2:
                    bGrid[i][j] = False
                return ans and ans2

            else:
                ans2 = checkNeighborBiggerSmaller(i,j,g,0,-1,False)
                if ans2:
                    bGrid[i][j-1] = False
                ans3 = checkNeighborBiggerSmaller(i,j,g,0,1,False)
                if ans3:
                    bGrid[i][j+1] = False
                return ans and ans2 and ans3
    else:
        # at most 4 neighbours
        if (j == 0 or j == width):
            # at most 3 neighbors
            if j == 0:
                ans = checkNeighborBiggerSmaller(i,j,g,0,1,False)
                if ans:
                    bGrid[i][j+1] = False
                ans2 = checkNeighborBiggerSmaller(i,j,g,-1,0,False)
                if ans2:
                    bGrid[i-1][j] = False
                ans3 = checkNeighborBiggerSmaller(i,j,g,1,0,False)
                if ans3:
                    bGrid[i+1][j] = False
                return ans and ans2 and ans3
            else: # j == width
                ans = checkNeighborBiggerSmaller(i,j,g,0,-1,False)
                if ans:
                    bGrid[i][j-1] = False
                ans2 = checkNeighborBiggerSmaller(i,j,g,-1,0,False)
                if ans2:
                    bGrid[i-1][j] = False
                ans3 = checkNeighborBiggerSmaller(i,j,g,1,0,False)
                if ans3:
                    bGrid[i+1][j] = False
                return ans and ans2 and ans3
        else:
            ans = checkNeighborBiggerSmaller(i,j,g,1,0,False)
            if ans:
                bGrid[i+1][j] = False
            ans2 = checkNeighborBiggerSmaller(i,j,g,0,1,False)
            if ans2:
                bGrid[i][j+1] = False
            ans3 = checkNeighborBiggerSmaller(i,j,g,-1,0,False)
            if ans3:
                bGrid[i-1][j] = False
            ans4 = checkNeighborBiggerSmaller(i,j,g,0,-1,False)
            if ans4:
                bGrid[i][j-1] = False
            return ans and ans2 and ans3 and ans4

with open(file) as f:
    lines = f.readlines()

grid = []
for line in lines:
    l = list(map(int, line.strip()))
    grid.append(l)

temp = (len(grid) * [True])
boolGrid =  []
for i in range(len(grid)):
    boolGrid.append(len(grid[0]) * [True])

# isSmallest(0, 1, grid, boolGrid)
# exit()

total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        ans = isSmallest(i, j, grid, boolGrid)
        if ans:
            total += grid[i][j]+1
        # print(ans)
print(total)
