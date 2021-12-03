file1 = open('input3.txt', 'r')

lines = file1.readlines()

count = 0
sumList = []

tree = {}

for line in lines:
    curr = line.strip()
    digits = list(curr)
    pos = 0
    treeLevel = tree
    for digit in digits:
        digit = int(digit)

        if (not digit in treeLevel):
            treeLevel[digit] = {}
            treeLevel[digit]['values'] = []
        treeLevel[digit]['values'].append(curr)
        treeLevel = treeLevel[digit]

        if (count == 0):
            sumList.append(digit)
        else:
            sumList[pos] += digit
        pos += 1       
    count += 1

print(f'List: {sumList}')
print(f'Total: {count}')
gamma = ''
epsilon = ''
pos = 0
for sum in sumList:
    if (sum >= count/2):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

    pos += 1

print(f'Gamma: {gamma} {int(gamma, 2)}')
print(f'Epsilon: {epsilon} {int(epsilon, 2)}')
print(f'Power: {int(gamma, 2) * int(epsilon, 2)}')

# Did it initially by recurive function, then realized
# I just needed to check the length of the lists :/
# def narrow(tree, pos, op):
#     curr_digit = 0
#     count = len(tree['values'])
#     for value in tree['values']:
#         curr_digit += int(list(value)[pos])

#     if (op == 1):
#         if (curr_digit >= count/2):
#             curr_digit = 1
#         else:
#             curr_digit = 0
#     else:
#         if (curr_digit >= count/2):
#             curr_digit = 0
#         else:
#             curr_digit = 1

#     if (len(tree[curr_digit]['values']) == 1):
#         return tree[curr_digit]['values'][0]
#     else:
#         return narrow(tree[curr_digit], pos+1, op)

o2 = tree[int(list(gamma)[0])]
while (len(o2['values']) > 1):
    if (len(o2[1]['values']) >= len(o2[0]['values'])):
        o2 = o2[1]
    else:
        o2 = o2[0]
o2 = o2['values'][0]
print(f'O2: {o2} {int(o2, 2)}')

co2 = tree[int(list(epsilon)[0])]
while (len(co2['values']) > 1):
    if (len(co2[1]['values']) >= len(co2[0]['values'])):
        co2 = co2[0]
    else:
        co2 = co2[1]
co2 = co2['values'][0]
print(f'CO2: {co2} {int(co2, 2)}')


# o2 = narrow(tree[int(list(gamma)[0])], 1, 1)
# co2 = narrow(tree[int(list(epsilon)[0])], 1, 0)
# print(f'O2: {o2} {int(o2, 2)}')
# print(f'CO2: {co2} {int(co2, 2)}')
print(f'Life Support: {int(o2, 2) * int(co2, 2)}')