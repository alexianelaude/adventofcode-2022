class Monkey:
    def __init__(self, items, op, test, monkeyTrue, monkeyFalse):
        self.items = items
        self.op = op
        self.test = test
        self.monkeyTrue = monkeyTrue
        self.monkeyFalse = monkeyFalse
        self.itemsInspected = 0

    def testAndThrow(self, item):
        return self.monkeyTrue if self.test(item) else self.monkeyFalse


ops = { "+": int.__add__, "*": int.__mul__ }

def createMonkeys():
    monkeyList = []
    with open('input/input11.txt', 'r') as f:
        lines = f.readlines()
        for i in range(0,56,7):
            items = [int(item.strip(',')) for item in lines[i+1].strip('\n').split(" ")[4:]]
            div = int(lines[i+3].strip('\n').split(" ").pop())
            (operator, b) = lines[i+2].strip('\n').split(" ")[-2:]
            monkeyTrue = int(lines[i+4].strip('\n').split(" ").pop())
            monkeyFalse = int(lines[i+5].strip('\n').split(" ").pop())
            monkeyList.append(Monkey(items, lambda x : ops[operator](x, x if b == 'old' else int(b)), lambda x : x % div == 0, monkeyTrue, monkeyFalse))
        f.close()
    return monkeyList

def runRound(monkeyList):
    for monkey in monkeyList:
        while len(monkey.items) > 0:
            monkey.itemsInspected += 1
            item = monkey.items.pop(0)
            new_worry = monkey.op(item)
            new_worry = new_worry // 3
            next_monkey = monkey.testAndThrow(new_worry)
            monkeyList[next_monkey].items.append(new_worry)
    return monkeyList

def part1():
    monkeyList = createMonkeys()
    for i in range(9):
        monkeyList = runRound(monkeyList)
    itemsInspectedList = sorted([monkey.itemsInspected for monkey in monkeyList])
    return itemsInspectedList[-1] * itemsInspectedList[-2]

print(part1())



