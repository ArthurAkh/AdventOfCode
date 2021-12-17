# file = 'fileTest'
file = 'file'

def findMinMax(listA, direction=0):
    if len(listA) == 1:
        return listA[0]
    if len(listA) < 2:
        return None
    if len(listA) == 2:
        if direction == -1:
            return min(listA[0], listA[1])
        return max(listA[0], listA[1])
    pop = listA.pop()
    ans = findMinMax(listA, direction)
    if direction == -1:
        return min(ans, pop)
    return max(ans, pop)

def compare(comparator, listToCompare, direction=0):
    comparatorChar = []
    for c in comparator:
        comparatorChar.append(c)

    listToCompareChar = []
    for l in listToCompare:
        lChar = []
        for c in l:
            lChar.append(c)
        listToCompareChar.append(lChar)


    index = 0
    listNotSame = len(listToCompare) * [0]
    for l in listToCompareChar:
        counter = 0
        for char in comparatorChar:
            for charT in l:
                if(char == charT):
                    counter+=1
                    break
        listNotSame[index] = len(comparatorChar) - counter
        index+=1

    ans = findMinMax(listNotSame.copy(), direction)
    index = listNotSame.index(int(ans))
    l = listToCompare[index]

    return ''.join(l)


with open(file) as f:
    lines = f.readlines()

listABC = []
for line in lines:
    strings = (line[:line.find("|")-1]).split(" ")
    digits = line[line.find("|")+1:].strip().split(" ")
    listABC.append([strings,digits])

# we know the length of digit 1, digit 4, 7 and 8
easyDigits = [2, 4, 3, 7]

#  AAA
# B   C
# B   C
#  DDD
# E   F
# E   F
#  GGG

# what we need to discover:
 # 2, 3, 5, 6, 9, 0

# we will deduce 6
# compare 1 to 6, 9, 0 to deduce which one is 6, that's the one without CCC
# then we will deduce 0 and 9
# compare 4 to 9 and 0 to deduce which one is 0, that's the one without DDD and the other one is 9
# then we will deduce 5
# we compare 6 to 2, 3, 5 to deduce 5 because 6 and 5 don't have EEE in common, but 2 and 3 don't have incommon BBB and (FFF or EEE)
# then we will deduce 2 and 3
# we will compare 1 to 2 and 3, 2 is the one that doesn't contain FFF, the other one is 3


sum = 0
for line in listABC:
    strings = line[0]

    # deduce 1, 4, 7, 8
    # and store the clues for 2, 3, 5 and for 6, 9, 0
    lenFive = [] # list for 2, 3, 5
    lenSix = []  # list for 6, 9, 0
    for clue in strings:
        length = len(clue)
        if (length == 2):
            one = clue
        elif (length == 4):
            four = clue
        elif (length == 3):
            seven = clue
        elif (length == 7):
            eight = clue
        elif (length == 5):
            lenFive.append(clue)
        else:
            lenSix.append(clue)

    # deduce 6
    six = compare(one, lenSix)
    lenSix.remove(six)
    # deduce 0
    zero = compare(four, lenSix)
    lenSix.remove(zero)
    # the last one is 9
    nine = lenSix[0]
    # deduce 5
    five = compare(six, lenFive, -1)
    lenFive.remove(five)
    # deduce 2
    two = compare(one, lenFive)
    lenFive.remove(two)
    # the last one is 3
    three = lenFive[0]
    digitsMapping = {2:two, 3:three, 5:five, 6:six, 9:nine, 0:zero}

    # for all digits
    digits = line[1]
    output = []
    for digit in digits:
        length = len(digit)
        if length == 7:
            output.append(8)
            continue
        elif length == 2:
            output.append(1)
            continue
        elif length == 4:
            output.append(4)
            continue
        elif length == 3:
            output.append(7)
            continue

        # find the corresponding clue
        for i, clue in digitsMapping.items():
            for charD in digit:
                appears = False
                for charC in clue:
                    if(charD == charC):
                        appears = True
                        break
                if (not appears):
                    break
            if (appears):
                output.append(i)
                break

    toAdd = int(''.join(list(map(str, output))))
    sum += toAdd
print(sum)
