import time
from queue import PriorityQueue

file = 'fileTest'
# file = 'file'
inf = 999999

def AStar(start):
    openSet = PriorityQueue()
    openSet.put((0, start.h(), start))
    start.fromStartToNode = 0

    closedSet = set()

    while openSet.qsize() > 0:
        current = openSet.get()[2]

        if current.end:
            return reconstruct_path(current)

        for node in current.getNeighbors():
            print("we're here")
            if node == current.parent:
                print("parent is here")
                continue
            print("we continue here")
            for nodeA in openSet.queue:
                print(nodeA)
            # print(closedSet)
            print()
            # time.sleep(1.5)
            nodeInOpenSetQueue = False
            for temp in openSet.queue:
                nodeCompare = temp[2]
                if node == nodeCompare:
                    nodeInOpenSetQueue = True
                    break

            if not nodeInOpenSetQueue and node not in closedSet:
                # print(closedSet)
                # time.sleep(1.5)
                openSet.put((current.fromStartToNode+node.weight, node.h(), node))
                node.fromStartToNode = current.fromStartToNode + node.weight
                node.parent = current
            else:
                if node.fromStartToNode > current.fromStartToNode + node.weight:
                    node.fromStartToNode = current.fromStartToNode + node.weight
                    node.parent = current

                if node in closedSet:
                    closedSet.remove(node)
                    openSet.put((current.fromStartToNode+node.weight, node.h(), node))


        closedSet.add(current)



def reconstruct_path(node):
    reconst_path = []

    while node.parent != node:
        reconst_path.append(node)
        node = node.parent
    reconst_path.reverse()
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
        self.goal = goal
        self.fromStartToNode = inf
        self.parent = None
        self.end = False

    def addNeighbor(self, i, j, node):
        if i == -1 and j == 0:
            self.n = node
        elif i == 1 and j == 0:
            self.s = node
        elif i == 0 and j == -1:
            self.w = node
        elif i == 0 and j == 1:
            self.e = node

    def h(self):
        x = self.goal.x - self.x
        y = self.goal.y - self.y
        return (x*x+y*y) ** (0.5)

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

    def __lt__(self, other):
        return self.h() < other.h()

if __name__ == '__main__':

    with open(file) as f:
        lines = f.readlines()


    grid = []
    for line in lines:
        line = line.strip()
        line = list(map(int, line))
        grid.append(line)

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
    for i in range(len(nodeList)):
        for j in range(len(nodeList[0])):
            node = nodeList[i][j]
            node.goal = goal
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

