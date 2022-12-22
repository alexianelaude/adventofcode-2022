def comparePairs(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return 2
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        rightOrder = 0
        i = 0
        while rightOrder == 0:
            if i >= min(len(left), len(right)):
                break
            rightOrder = comparePairs(left[i], right[i])
            i += 1
        if rightOrder != 0:
            return rightOrder
        if len(left) <= i:
            return 1
        if len(right) <= i:
            return 2
        return rightOrder
    elif isinstance(left, int):
        return comparePairs([left], right)
    else:
        return comparePairs(left, [right])

def buildPair(line):
    all_list = []
    for char in line:
        if char == '[':
            all_list.append([])
        elif char == ']':
            finished_list = all_list.pop()
            if len(all_list) > 0:
                all_list[-1].append(finished_list)
            else:
                all_list = [finished_list]
        elif char != ',':
            all_list[-1].append(int(char))
    return all_list[0]


def buildPairs():
    with open('input/input13.txt', 'r') as f:
        lines = [line.strip('\n') for line in f.readlines()]
        sum = 0
        for i in range(0,len(lines),3):
            left = buildPair(lines[i])
            right = buildPair(lines[i+1])
            pairIx = (i // 3) + 1
            print(pairIx)
            if comparePairs(left, right) == 1:
                sum += pairIx
        f.close()
    return sum

print(buildPairs())
