from string import ascii_letters
file = [l.strip() for l in open('day3.txt')]

# Part 1 - Common character between a line split in 2
def part1(data):
    total = 0
    for line in data:
        l1, l2 = line[:len(line)//2], line[len(line)//2:]
        common = ''.join(set(l1) & set(l2))
        total += ascii_letters.index(common) + 1
    return total

# Part 2 - Common character between 3 lines
def part2(data):
    total = 0
    for line in range(0, len(data), 3):
        l1, l2, l3 = data[line:line+3]
        common = ''.join(set(l1) & set(l2) & set(l3))
        total += ascii_letters.index(common) + 1
    return total

print('Part 1: ', part1(file))
print('Part 2: ', part2(file))