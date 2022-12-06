file = [l.strip() for l in open('day6.txt')]

# Part 1 - First 4 unique chars
def part1(data):
    str = data[0]
    for i in range(4, len(str)):
        tmp = str[i-4:i]
        if len(set(tmp)) == 4:
            return i

# Part 2 - First 14 unique chars
def part2(data):
    str = data[0]
    for i in range(14, len(str)):
        tmp = str[i-14:i]
        if len(set(tmp)) == 14:
            return i

print("Part 1: ", part1(file))
print("Part 2: ", part2(file))