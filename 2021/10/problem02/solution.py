import math

# file = 'fileTest'
file = 'file'

def determinePrice(c):
    if c == ")":
        ans = 3
    elif c == "]":
        ans = 57
    elif c == "}":
        ans = 1197
    elif c == ">":
        ans = 25137
    else:
        ans = 0
    return ans

class stackOfCharacters:
    def __init__(self, node=None):
        self.firstNode = node

    def push(self, node):
        oldFirst = self.firstNode
        if oldFirst != None:
            oldFirst.previous = node
            node.next = oldFirst
        self.firstNode = node

    def resolve(self):
        if self.firstNode.next.expected == self.firstNode.val:
            self.firstNode = self.firstNode.next.next
            return True
        return False

        # itr = self.firstNode.next
        # while itr != None:
        #     if itr.expected == self.firstNode.val:
        #         itr.previous.next = itr.next
        #         if(itr.next != None):
        #             itr.next.previous = itr.previous

        #         if(self.firstNode.next != None):
        #             self.firstNode = self.firstNode.next
        #             self.firstNode.previous = None
        #         return True
        #     itr = itr.next
        return False

    def complete(self):
        total = 0

        itr = self.firstNode
        while itr != None:
            c = itr.expected

            if c == ")":
                ans = 1
            elif c == "]":
                ans = 2
            elif c == "}":
                ans = 3
            elif c == ">":
                ans = 4
            else:
                ans = 0

            total*=5
            total+=ans
            itr = itr.next

        return total



class node:
    def __init__(self, val=None, expected=None):
        self.val = val
        self.expected = expected
        self.previous = None
        self.next = None


with open(file) as f:
    lines = f.readlines()


grid = []
for line in lines:
    l = line.strip()
    grid.append(l)

stacks = []
for line in grid:
    stack = stackOfCharacters()
    addLine = True
    for c in line:
        needsResolution = False
        if c == "(":
            expected = ")"
        elif c == "[":
            expected = "]"
        elif c == "{":
            expected = "}"
        elif c == "<":
            expected = ">"
        else:
            needsResolution = True
            expected = None

        character = node(c, expected)
        stack.push(character)
        if needsResolution and not stack.resolve():
            addLine = False
            break
    if addLine:
        stacks.append(stack)

totalList = []
for stack in stacks:
    totalList.append(stack.complete())

totalList.sort()
print(totalList[math.floor(len(totalList)/2)])
