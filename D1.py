
def groupCalories():
    with open('input/input1.txt', 'r') as f:
        lines = f.readlines()
        currentGroup = []
        allGroups = []
        for line in lines:
            if line == '\n':
                allGroups.append(currentGroup)
                currentGroup = []
            else:
                currentGroup.append(int(line))
        f.close()
    return allGroups

def part1():
    calories = groupCalories()
    max_cal = 0
    for group in calories:
        cal_sum = sum(group)
        if cal_sum > max_cal:
            max_cal = cal_sum
    return max_cal

def part2():
    calories = groupCalories()
    top_three = [0, 0, 0] #in ascending order
    for group in calories:
        cal_sum = sum(group)
        if cal_sum > top_three[0]:
            top_three[0] = cal_sum
            top_three.sort()
    return sum(top_three)
