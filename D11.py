class Monkey:
    def __init__(self, items, op, test, monkeyTrue, monkeyFalse):
        self.items = items
        self.op = op
        self.test = test
        self.monkeyTrue = monkeyTrue
        self.monkeyFalse = monkeyFalse
        self.itemsInspected = 0

    def testAndThrow(item):
        self.monkeyTrue if self.test(item) else self.monkeyFalse


ops = { "+": int.__add__, "*": int.__mul__ }

def createMonkeys():
    monkeyList = []
    with open('input/input11.txt', 'r') as f:
        lines = f.readlines()
        for i in range(0,56,7):
            items = [int(item.strip(',')) for item in lines[i+1].strip('\n').split(" ")[4:]]
            div = int(lines[i+3].strip('\n').split(" ").pop())
            test = lambda x : x % div == 0
            (operator, b) = lines[i+2].strip('\n').split(" ")[-2:]
            operator = ops[operator]
            op = lambda x : operator(x, x if b == 'old' else int(b))
            monkeyTrue = int(lines[i+4].strip('\n').split(" ").pop())
            monkeyFalse = int(lines[i+5].strip('\n').split(" ").pop())
            monkeyList.append(Monkey(items,op,test, monkeyTrue, monkeyFalse))
        f.close()
    return monkeyList

print(createMonkeys())





