file = 'fileTest'
# file = 'file'


def simulateRule(char, rule, rules, step):
    if simulations.get(rule+'_'+str(step)) != None:
        return simulations.get(rule+'_'+str(step))

    letters = []
    simulations.update({rule[0]+'_'+str(step):letters})


def simulate(chars, rules, steps, printed = True):
    # if (printed == False):
        # print(steps)
    # print("entering simulate with chars:", chars, "steps:", steps)
    if steps <= 0:
        return {}

    chars2 = applyRules(chars, rules)

    countLetters = {}

    if len(chars2) > 0:
        countLetters.update({chars2:1})
        # print("printing countLetters:", countLetters)
        # print("entering count1")
        count1 = simulate(chars[0] + chars2, rules, steps-1, False)
        # print("entering count2")
        count2 = simulate(chars2 + chars[1], rules, steps-1)

        for char, num in count1.items():
            if countLetters.get(char) == None:
                countLetters.update({char:num})
            else:
                countLetters.update({char:countLetters.get(char) + num})

        for char, num in count2.items():
            if countLetters.get(char) == None:
                countLetters.update({char:num})
            else:
                countLetters.update({char:countLetters.get(char) + num})

    return countLetters

def applyRules(chars, rules):
    for j in range(len(rules)):
        if chars == rules[j][0]:
            return rules[j][1][1:2]
    return ''


if __name__ == '__main__':

    with open(file) as f:
        lines = f.readlines()

    string = lines.pop(0).strip()
    lines.pop(0)

    insRules = []
    for line in lines:
        l = line.strip().split(" -> ")
        l[1] = l[0][0] + l[1] + l[0][1]
       insRules.append(l)
# print(insRules)

    letters = {}
    lettersDict = {}
    for c in string:
        letters.update({c:0})
        lettersDict.update({c:0})
    global simulations = {}
# for rule in insRules:
#     simulations.update({rule[0]+'_'+str(step):letters})

    for rule in insRules:
        letters.update({rule[1][1:2]:0})
    for c in string:
        letters.update({c:letters.get(c)+1})

    simulateRule()
    exit()

    for i in range(len(string)-1):
        chars = string[i:i+2]
        tempLetters = simulate(chars, insRules, 40)
        for char, num in tempLetters.items():
            letters.update({char:letters.get(char) + num})

    numbers = []
    for num in letters.values():
        numbers.append(num)

    numbers.sort()

    print(numbers[len(numbers)-1] - numbers[0])
# letters.get()
