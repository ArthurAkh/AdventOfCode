from queue import PriorityQueue
import time

file = 'fileTest'
# file = 'file'

grid = []

class State(object):
    def __init__(self, value, parent, start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0

        if parent:
            self.start = parent.start
            self.goal = parent.goal
            self.path = parent.path[:]
            self.path.append(value)

        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def getDist(self):
        pass

    def getChildren(self):
        pass

class State_String(State):
    def __init__(self, value, parent, start = 0, goal = 0):
        super(State_String, self).__init__(value, parent, start, goal)
        self.dist = self.getDist()

    def getDist(self):
        if self.value == self.goal:
            return [0, 0]
        dist = []
        dist.append(self.goal[0]-self.value[0])
        dist.append(self.goal[1]-self.value[1])
        return dist

    def createChildren(self):
        if not self.children:

            val = [self.value[0], self.value[1]-1]
            if val[0] >= 0 and val[0] < len(grid[0]) and val[1] >= 0 and val[1] < len(grid):
                child = State_String(val, self)
                self.children.append(child)
            val = [self.value[0]+1, self.value[1]]
            if val[0] >= 0 and val[0] < len(grid[0]) and val[1] >= 0 and val[1] < len(grid):
                child = State_String(val, self)
                self.children.append(child)
            val = [self.value[0], self.value[1]+1]
            if val[0] >= 0 and val[0] < len(grid[0]) and val[1] >= 0 and val[1] < len(grid):
                child = State_String(val, self)
                self.children.append(child)
            val = [self.value[0]-1, self.value[1]]
            if val[0] >= 0 and val[0] < len(grid[0]) and val[1] >= 0 and val[1] < len(grid):
                child = State_String(val, self)
                self.children.append(child)

class AStarSolver:
    def __init__(self, start, goal, grid):
        self.path = []
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal
        self.grid = grid

    def solve(self):
        startState = State_String(self.start, 0, self.start, self.goal)
        # print(startState.goal, startState.value, startState.dist)
        count = 0
        self.priorityQueue.put((0, count, startState))

        while(not self.path and self.priorityQueue.qsize()):
            closestChild = self.priorityQueue.get()[2]
            closestChild.createChildren()
            self.visitedQueue.append(closestChild.value)
            for child in closestChild.children:
                print("child in closestChild", child.value)
                print("visited children", self.visitedQueue)
                if child.value not in self.visitedQueue:
                    count += self.grid[child.value[0]][child.value[1]]
                    print(count)
                    print("child path", child.path)
                    print("child dist", child.dist)
                    print()
                    time.sleep(0.5)
                    # if not child.dist:
                    if child.dist == [0, 0]:
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.dist, count, child))
        if not self.path:
            print("Goal is impossible", self.goal)
        return self.path

if __name__ == '__main__':

    with open(file) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        line = list(map(int, line))
        grid.append(line)
    start = [0, 0]
    goal = [len(grid[0])-1, len(grid)-1]
    print("Starting...")
    a = AStarSolver(start, goal, grid)
    a.solve()
    print(a.path)
