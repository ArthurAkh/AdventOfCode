# file = 'fileTest'
file = 'file'

def createNode(i, j, g, n):
    if i < 0 or i >= len(g) or j < 0 or j >= len(g[0]):
        return None

    node = nodes(g[i][j])
    n[i][j] = node
    return node

def deleteNeighbors(node):
    if node.n != None:
        node.n.s = None
    if node.w != None:
        node.w.e = None
    if node.e != None:
        node.e.w = None
    if node.s != None:
        node.s.n = None
    node.n = node.w = node.e = node.s = None


def assigneNeighbors(i, j, n):
    node = n[i][j]

    if(i > 0):
        node.n = n[i-1][j]
    if(j > 0):
        node.w = n[i][j-1]
    if(j < len(n[0])-1):
        node.e = n[i][j+1]
    if(i < len(n)-1):
        node.s = n[i+1][j]

def calculateSum(node):
    if node == None or node.visited:
        return 0
    node.visited = True
    node.teamLeader = node
    # sumTotal = node.val
    sumTotal = 1
    sumTotal += calculateSumPrivate(node.n, node)
    sumTotal += calculateSumPrivate(node.w, node)
    sumTotal += calculateSumPrivate(node.e, node)
    sumTotal += calculateSumPrivate(node.s, node)
    node.sum = sumTotal

    return sumTotal

def calculateSumPrivate(node, teamLeader):
    if node == None or node.visited:
        return 0
    node.visited = True
    node.teamLeader = teamLeader
    # sumTotal = node.val
    sumTotal = 1
    sumTotal += calculateSumPrivate(node.n, teamLeader)
    sumTotal += calculateSumPrivate(node.w, teamLeader)
    sumTotal += calculateSumPrivate(node.e, teamLeader)
    sumTotal += calculateSumPrivate(node.s, teamLeader)
    node.sum = sumTotal

    return sumTotal




class nodes:
    def __init__(self, val=None, n=None, w=None, e=None, s=None):
        self.val = val
        self.visited = False
        self.n = n
        self.w = w
        self.e = e
        self.s = s
        self.teamLeader = None
        self.sum = 0

with open(file) as f:
    lines = f.readlines()

grid = []
for line in lines:
    l = list(map(int, line.strip()))
    grid.append(l)
# print(grid)
# exit()

boolGrid = []
boolLine = len(grid[0]) * [False]
for i in range(len(grid)):
    boolGrid.append(boolLine)

node = nodes()
nodeArray = []
for i in range(len(grid)):
    temp = len(grid[0]) * [None]
    nodeArray.append(temp)


# nodeList = createNode(0, 0, grid, boolGrid, nodeArray)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        # print("creating " + str(i) + ", " +str(j))
        # node = createNode(i, j, grid, boolGrid, nodeArray)
        node = createNode(i, j, grid, nodeArray)
        # print(node.val)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        assigneNeighbors(i, j, nodeArray)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if(nodeArray[i][j].val == 9):
            deleteNeighbors(nodeArray[i][j])

for i in range(len(grid)):
    for j in range(len(grid[0])):
        calculateSum(nodeArray[i][j])

listMax = [0, 0, 0]
ignoreLeaders = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if nodeArray[i][j].teamLeader != None:
            newLeader = True
            for leader in ignoreLeaders:
                if(newLeader and leader == nodeArray[i][j].teamLeader):
                    newLeader = False

            if newLeader:
                new = nodeArray[i][j].teamLeader.sum
                if(new > listMax[0]):
                    ignoreLeaders.append(nodeArray[i][j].teamLeader)
                listMax[0] = max(listMax[0], new)
                listMax.sort()

print(listMax[0]*listMax[1]*listMax[2])
