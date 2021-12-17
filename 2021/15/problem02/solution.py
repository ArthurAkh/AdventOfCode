import time

# file = "fileTest"
file = "file"
inf = 999999

def incrementMap(line):
    newLine = []
    tempChar = []
    for n in line:
        newLine.append(increment(n))

    return newLine


    for line in smallGrid:
        temp = []
        newLine = line
        for i in range(5):
            for n in newLine:
                temp.append(n)
            newLine = list(map(increment, newLine))
        grid.append(temp)


def increment(n):
    new = n+1
    if new > 9:
        new = 1
    return new

def reconstruct_path(node):
    reconst_path = []
    weight = 0

    while node.parent != None:
        weight += node.weight
        reconst_path.append([node.y, node.x])
        node = node.parent
    reconst_path.reverse()
    print(weight)
    return reconst_path


class nodeClass:
    def __init__(self, weight, x, y, goal = None):
        self.weight = weight
        self.x = x
        self.y = y
        self.n = None
        self.e = None
        self.s = None
        self.w = None
        self.h = None
        self.goal = goal
        self.g = 0
        self.f = inf
        self.parent = None
        self.end = False

    def printInfo(self):
        if self.parent != None:
            print("x:", self.x, "y:", self.y, "weight:", self.weight, "g:", self.g, "f:", self.f, "parent:", self.parent.x, self.parent.y)
            return
        print("x:", self.x, "y:", self.y, "weight:", self.weight, "g:", self.g, "f:", self.f, "parent: None", )

    def addNeighbor(self, i, j, node):
        if i == -1 and j == 0:
            self.n = node
        elif i == 1 and j == 0:
            self.s = node
        elif i == 0 and j == -1:
            self.w = node
        elif i == 0 and j == 1:
            self.e = node

    def heu(self):
        x = abs(self.goal.x - self.x)
        y = abs(self.goal.y - self.y)
        return x+y

    def getNeighbors(self):
        neighbors = []
        if self.n != None:
            neighbors.append(self.n)
        if self.s != None:
            neighbors.append(self.s)
        if self.w != None:
            neighbors.append(self.w)
        if self.e != None:
            neighbors.append(self.e)
        return neighbors



def AStar(start):
    openList = []
    closedList = []

    openList.append(start)
    start.f = 0

    while len(openList) > 0:
        minimalF = inf
        minimalFIndex = -1
        for i in range(len(openList)):
            node = openList[i]
            if minimalF > node.f:
                minimalF = node.f
                minimalFIndex = i
        if minimalF == inf:
            print("bad")
            exit()
        node = openList[minimalFIndex]
        openList.remove(node)
        closedList.append(node)
        for successor in node.getNeighbors():
            # successor.printInfo()
            if successor.end:
                successor.parent = node
                return reconstruct_path(successor)
            elif successor not in closedList:
                newG = node.g + successor.weight
                newF = newG + successor.h
                # print("newG:", newG, "newF:", newF)

                if successor not in openList or successor.f > newF:
                    # print("successor not in openList or sucessor.f > newF")
                    # print("newF:", newF, "successor.f:", successor.f)
                    openList.append(successor)
                    successor.parent = node
                    successor.g = newG
                    successor.f = newF
            # successor.printInfo()
            # print()
            # time.sleep(2.5)

if __name__ == '__main__':
    with open(file) as f:
        lines = f.readlines()

    smallGrid = []
    for line in lines:
        line = line.strip()
        line = list(map(int, line))
        smallGrid.append(line)

    grid = []
    for j in range(5):
        for line in smallGrid:
            temp = []
            newLine = line
            for i in range(5):
                for n in newLine:
                    temp.append(n)
                newLine = list(map(increment, newLine))
            grid.append(temp)
        smallGrid = list(map(incrementMap, smallGrid))


    nodeList = []
    for i in range(len(grid)):
        temp = []
        for j in range(len(grid[0])):
            g = grid[i][j]
            n = nodeClass(g, j, i)
            temp.append(n)
        nodeList.append(temp)

    nodeList[len(nodeList)-1][len(nodeList[0])-1].end = True

    start = nodeList[0][0]
    goal = nodeList[len(nodeList)-1][len(nodeList[0])-1]
    goal.end = True
    for i in range(len(nodeList)):
        for j in range(len(nodeList[0])):
            node = nodeList[i][j]
            node.goal = goal
            node.h = node.heu()
            if i-1 >= 0:
                if node.n == None:
                    north = nodeList[i-1][j]
                    node.addNeighbor(-1, 0, north)
                    north.addNeighbor(1, 0, node)
            if i+1 < len(nodeList):
                if node.s == None:
                    south = nodeList[i+1][j]
                    node.addNeighbor(1, 0, south)
                    south.addNeighbor(-1, 0, node)

            if j-1 >= 0:
                if node.w == None:
                    west = nodeList[i][j-1]
                    node.addNeighbor(0, -1, west)
                    west.addNeighbor(0, 1, node)
            if j+1 < len(nodeList[0]):
                if node.e == None:
                    east = nodeList[i][j+1]
                    node.addNeighbor(0, 1, east)
                    east.addNeighbor(0, -1, node)

    print(AStar(start))
    print(goal.parent.g+goal.weight)
