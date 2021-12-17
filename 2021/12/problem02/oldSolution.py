# file = 'fileTest'
# file = 'fileTest2'
# file = 'fileTest3'
file = 'file'

class nodeC:
    def __init__(self, val=None):
        self.val = val
        self.isBig = self.val.isupper()
        self.list = []
        self.visited = False

    def link(self, n):
        self.list.append(n)
        n.list.append(self)

    def findPathsStart(self, dist, pList):
        # print("starting")
        # print(self.val, dist)
        # print()
        nmbPaths = 0
        for neighbor in self.list:
            nmbPaths += neighbor.findPaths(dist-1, self.val, pList, [self.val])
            self.completeReset()
        return nmbPaths

    def findPaths(self, dist, valPrevious, pList, pathHistory = []):
        if self.val == "start" and valPrevious != None:
            return 0
        if dist < 0:
            return 0
        if self.visited and not self.isBig:
            return 0
        # print("dist is", dist, valPrevious, self.val)
        if self.val == "end":
            if dist == 0:
                pathHistory.append(self.val)
                pList.append(pathHistory)
                # print(pList)
                # exit()
                return 1
            else:
                return 0
        if self.val != "start":
            self.visited = True
        nmbPaths = 0
        myPath = pathHistory.copy()
        myPath.append(self.val)
        # print("pathHistory", pathHistory)
        # print("myPath", myPath)
        for neighbor in self.list:
            nmbPaths += neighbor.findPaths(dist-1, self.val, pList, myPath)
        self.visited = False
        return nmbPaths

    def completeReset(self):
        self.reset()
        for neighbor in self.list:
            if neighbor.visited:
                neighbor.completeReset()

    def reset(self):
        self.visited = False

def createNode(val, l):
    for node in l:
        if node.val == val:
            return node
    node = nodeC(val)
    l.append(node)
    return node

with open(file) as f:
    lines = f.readlines()

listNodes = []
for line in lines:
    l = line.strip()
    temp = []
    temp.append(l[:l.find("-")])
    temp.append(l[l.find("-")+1:])
    node1 = createNode(temp[0], listNodes)
    node2 = createNode(temp[1], listNodes)
    node1.link(node2)

# traverse from start to end

startNode = None
for node in listNodes:
    if node.val == "start":
        startNode = node
        break
# test
# pathList = []
# startNode.findPathsStart(4, pathList)
# print(pathList)
# exit()

initialD = 1
pathList = []
while(initialD < 2*len(listNodes)):
    dist = initialD
    startNode.findPathsStart(dist, pathList)
    initialD += 1
# print(pathList)
print(len(pathList))
