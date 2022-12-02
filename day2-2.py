# A/X = rock
# B/Y = paper
# C/Z = scissors

data = []
total = 0
f = open('day2.txt', 'r')

# Append file to a list
for line in f:
    data.append(line.strip())

# RPS battle
# X = lose, Y = draw, Z = win
for i in data:
    # Rock
    if (i[0] == 'A'):
        if (i[2] == 'X'):
            total+=3
        if (i[2] == 'Y'):
            total+=1
            total+=3
        if (i[2] == 'Z'):
            total+=2
            total+=6
    # Paper
    if (i[0] == 'B'):
        if (i[2] == 'X'):
            total+=1
        if (i[2] == 'Y'):
            total+=2
            total+=3
        if (i[2] == 'Z'):
            total+=3
            total+=6
    # Scissors
    if (i[0] == 'C'):
        if (i[2] == 'X'):
            total+=2
        if (i[2] == 'Y'):
            total+=3
            total+=3
        if (i[2] == 'Z'):
            total+=1
            total+=6

print(total)