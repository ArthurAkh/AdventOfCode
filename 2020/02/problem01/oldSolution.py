# file = 'fileTest'
file = 'file'

def test(i, j, k, array, valueDict):
    min1 = min(i, j)
    min1 = min(min1, k)
    if(min1 == i):
        min2 = min(j, k)
        min3 = max(j, k)
    elif(min1 == j):
        min2 = min(i, k)
        min3 = max(i, k)
    else:
        min2 = min(i, j)
        min3 = max(i, j)

    key = str(min1) + "-" + str(min2) + "-" + str(min3)
    if key in valueDict:
        # print("key in dictionnary :" + key)
        return valueDict.get(key)
    temp = numbers[i] + numbers[j] + numbers[k]
    valueDict[key] = temp
    return temp



with open(file) as f:
    lines = f.readlines()

numbers = []
for line in lines:
    numbers.append(int(line.strip()))

# numbers.sort()
# print(numbers)
# print(len(numbers))
# exit()

valueDict = {}
for i in range(len(numbers)):
    for j in range(len(numbers)):
        for k in range(len(numbers)):
            if(i != j and i != k and j != k):
                temp = test(i,j,k, numbers, valueDict)
                if temp == 2020:
                    print(str(temp) + " = " + str(numbers[i]) + " + " + str(numbers[j]) + " + " + str(numbers[k]))
                    print(str(numbers[i] * numbers[j] * numbers[k]))
                    exit()
