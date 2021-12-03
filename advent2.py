file1 = open('input2.txt', 'r')

lines = file1.readlines()

pos = 0
depth = 0
aim = 0

for line in lines:
    curr = line.strip()
    [command, amount] = curr.split()
    unit = int(amount)
    if (command == 'forward'):
        pos += unit
        depth += aim * unit
    elif (command == 'down'):
        aim += unit
    elif (command == 'up'):
        aim -= unit
    else:
        print(f'opps {curr}') 

print(f'Position: {pos}')
print(f'Depth: {depth}')
print(f'Multiply: {depth*pos}')