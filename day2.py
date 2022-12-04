file = [l.strip() for l in open('day2.txt')]

# Part 1 - Lookup values and add total points
def part1(data):
    total = 0
    points = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }
    for i in data:
        total += points.get(i)
    return total

# Part 2 - X - Lose, Y - Draw, Z - Win
def part2(data):
    total = 0
    points = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }
    for i in data:
        total += points.get(i)
    return total

print("Part 1: ", part1(file))
print("Part 2: ", part2(file))