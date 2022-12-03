items = [l.strip() for l in open('day3.txt')]
total = 0
total2 = 0
string1 = []
string2 = []
common = []
common2 = []

letters = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39, 
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
}

# Split string into separate lists
for i in items:
    string1.append(i[:len(i)//2])
    string2.append(i[len(i)//2:])

# Find common letter in split strings
for i in range(len(string1)):
    common.append(''.join(set(string1[i]).intersection(string2[i])))

# Get totals from letters
for i in range(len(common)):
    total += letters.get(common[i])

# Part 2 - compare strings for 3 items
count = 0
while count < len(items):
    tmp1 = (set(items[count]).intersection(items[count+1]))
    tmp2 = (set(items[count+2]).intersection(tmp1))
    common2.append(''.join(tmp2))
    count += 3

# Get totals from letters
for i in range(len(common2)):
    total2 += letters.get(common2[i])

print("part 1:", total)
print("part 2:", total2)