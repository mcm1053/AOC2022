file = [l.strip() for l in open('day5.txt')]
file2 = [l.replace('    ','[0]').replace('][', '] [').replace('\n','').replace('[','').replace(']','').split(' ') for l in open('day5.txt')]

# Part 1 - Stacks
def part1(data, data2):
    operations = []
    guide = []
    stack = [[], [], [], [], [], [], [], [], []]
    answer = []

    # Guide formatting
    for i in range(8):
        guide.append(data2[i])
    guide.reverse()
    # print(guide[1][0])
    for i in range(9):
        for k in range(len(guide)):
            stack[i].append(guide[k][i])
    for i in range(len(stack)):
        while '0' in stack[i]: stack[i].remove('0')    

    # Operations formatting
    for i in range(10,len(data)):
        operations.append(data[i])
    for i in range(len(operations)):
        tmp = operations[i].replace('move','').replace('from',',').replace('to',',').replace(' ','').split(',')

        # [0]Amnt - [1]From - [2]To
        # Pop values x times from y list
        for k in range(int(tmp[0])):
            stack[(int(tmp[2])-1)].append(stack[int(tmp[1])-1].pop())

    # Answer formatting
    for i in range(len(stack)):
        answer.append(stack[i].pop())
    return ''.join([str(i) for i in answer])

# Part 2 - Retain order
def part2(data, data2):
    operations = []
    guide = []
    stack = [[], [], [], [], [], [], [], [], []]
    answer = []
    mx = []

    # Guide formatting
    for i in range(8):
        guide.append(data2[i])
    guide.reverse()
    # print(guide[1][0])
    for i in range(9):
        for k in range(len(guide)):
            stack[i].append(guide[k][i])
    for i in range(len(stack)):
        while '0' in stack[i]: stack[i].remove('0')    

    # Operations formatting
    for i in range(10,len(data)):
        operations.append(data[i])
    for i in range(len(operations)):
        tmp = operations[i].replace('move','').replace('from',',').replace('to',',').replace(' ','').split(',')

        # [0]Amnt - [1]From - [2]To
        # Pop values x times from y list
        for k in range(int(tmp[0])):
            mx.append(stack[int(tmp[1])-1].pop())
        mx.reverse()
        for l in range(len(mx)):
            stack[(int(tmp[2])-1)].append(mx[l])
        mx = []

    # Answer formatting
    for i in range(len(stack)):
        answer.append(stack[i].pop())
    return ''.join([str(i) for i in answer])
        
print("Part 1: ", part1(file, file2))
print("Part 2: ", part2(file, file2))