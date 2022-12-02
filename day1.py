file = open('day1.txt','r')
data = []
totals = []

# Each line from file into list
for line in file:
    data.append(line.strip())

# Parse list
tmp = 0
for i in data:
    if len(i)==0:
        totals.append(tmp)
        tmp = 0
        continue
    tmp += int(i)

totals.sort(reverse=True)

# Most
print(totals[1])
# Top three
print(totals[1]+totals[2]+totals[3])