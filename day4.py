file = [l.strip() for l in open('day4.txt')]

# Part 1 - Contains range
def part1(data):
    count = 0
    for i in range(len(data)):
        ranges = data[i]
        convert = ranges.replace("-",",").split(",")
        toint = [eval(i) for i in convert]
        if toint[0] <= toint[2] <= toint[3] <= toint[1] or toint[2] <= toint[0] <= toint[1] <= toint[3]:
            count += 1
    return count

# Part 2 - Any overlap
def part2(data):
    count = 0
    for i in range(len(data)):
        ranges = data[i]
        convert = ranges.replace("-",",").split(",")
        toint = [eval(i) for i in convert]
        if toint[1] >= toint[2] and toint[0] <= toint[3] or toint[3] >= toint[0] and toint[2] <= toint[1]:
            print(toint)
            count += 1
    return count


print("Part 1: ", part1(file)) 
print("Part 2: ", part2(file)) 