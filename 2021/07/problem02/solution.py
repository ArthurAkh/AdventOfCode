import time

# file = 'fileTest'
file = 'file'

def calculateFuel(dist):
    if(distFuel[dist] == -1):
        distFuel[dist] = (dist * (dist+1)) / 2
    return distFuel[dist]

with open(file) as f:
    lines = f.readlines()

numbersStr = lines[0].strip().split(',')

numbers = []
for number in numbersStr:
    numbers.append(int(number))

maximum = max(numbers)+1
minimum = min(numbers)

positions = (maximum - minimum) * [0]
distFuel = (maximum - minimum) * [-1]

for pos in range(len(positions)):
    for i in range (len(numbers)):
        dist = abs(numbers[i]-pos)
        neededFuel = calculateFuel(dist)
        positions[pos] += neededFuel
        # print("position["+ str(pos) +"] is " + str(positions[pos]) + ", and " + str(neededFuel) + " was just added, where numbers[" + str(i) + "] = " + str(numbers[i]) + ".")

minFuel = min(positions)

print(int(minFuel))
