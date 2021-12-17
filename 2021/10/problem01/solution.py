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
    # l = list(map(int, line.strip()))
    l = line.strip()
    grid.append(l)

illegalSum = 0
for line in grid:
    stack = stackOfCharacters()
    debug = 0
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
            illegalSum += determinePrice(c)
            break
        if debug == 1000:
            print("debug")
            print(c)
            print(needsResolution)
            print(stack.firstNode.val)
            exit()
        debug+=1

print(illegalSum)
