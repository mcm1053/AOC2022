file = [l.strip() for l in open('day1.txt')]

# Part 1 - Max values in group
def part1(data):
    tmp = 0 
    totals = []
    for i in data:
        if len(i) == 0:
            totals.append(tmp)
            tmp = 0
            continue
        tmp += int(i)
    totals.sort(reverse=True)
    return(totals[0])

# Part 2 - Top 3 values
def part2(data):
    tmp = 0 
    totals = []
    for i in data:
        if len(i) == 0:
            totals.append(tmp)
            tmp = 0
            continue
        tmp += int(i)
    totals.sort(reverse=True)
    return(totals[0] + totals[1] + totals[2])

print("Part 1: ", part1(file))
print("Part 2: ", part2(file))