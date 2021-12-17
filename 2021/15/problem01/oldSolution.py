from queue import PriorityQueue

class State(object):
    def __init__(self, value, parent, start = 0, goal = 0):
        self.children = []    #Children is a list of all membering possibilities
        self.parent = parent  #store current parent
        self.value = value    #store current value
        self.dist = 0         #store current distance, dist is not actually gonna be set
                              #here, it is just a placeholder. It actually meant to be set to sub state
                              #or subclasses of State class
    if parent:
        self.start = parent.start
        self.goal = parent.goal
        self.path = parent.path[:]
        self.path.append(value)
    else:
        self.path = [value]
        self.start = start
        self.goal = goal

    def GetDistance(self):
        pass
    def CreateChildren(self):
        pass


# Creating subclass
class State_String(State):
    def __init__(self, value, parent, start = 0, goal = 0 ):
        super(State_String, self).__init__(value, parent, start, goal)
        self.dist = self.GetDistance()

    def GetDistance(self):
        if self.value == self.goal:
            return 0
        dist = []
        dist[0] = abs(self.goal[0] - self.value[0])
        dist[1] = abs(self.goal[1] - self.value[1])
        # for i in range(len(self.goal)):
        #     letter = self.goal[i]
        #     dist += abs(i - self.value.index(letter))
        return dist

    def CreateChildren(self):
        if not self.children:

# Creating a class that hold the final magic
class A_Star_Solver:
    def __init__(self, start, goal):
        self.path = []
        self.vistedQueue =[]
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def Solve(self):
        startState = State_String(self.start,0,self.start,self.goal)

        count = 0
        self.priorityQueue.put((0,count, startState))
        while(not self.path and self.priorityQueue.qsize()):
            closesetChild = self.priorityQueue.get()[2]
            closesetChild.CreateChildren()
            self.vistedQueue.append(closesetChild.value)
            for child in closesetChild.children:
                if child.value not in self.vistedQueue:
                    count += child.value
                    if not child.dist:
                        self.path = child.path
                    self.priorityQueue.put((child.dist,count,child))
        if not self.path:
            print("Goal Of  is not possible !" + self.goal )
        return self.path



file = 'fileTest'
# file = 'file'

if __name__ == '__main__':

    with open(file) as f:
        lines = f.readlines()

    grid = []
    for line in lines:
        grid.append(line.strip())
    print(grid)
    star1 = [0, 0]
    goal1 = [len(grid[0]-1, len(grid)-1)]
    print("starting...")
    a = A_Star_Solver(start1, goal1)
    a.Solve()
