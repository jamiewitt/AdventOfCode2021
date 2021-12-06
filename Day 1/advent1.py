file1 = open('input.txt', 'r')

lines = file1.readlines()

count = 0
prevSum = -1
sumParts = []
currSum = -1

for line in lines:
    curr = int(line.strip())
    sumParts.append(curr)

    if (len(sumParts) == 3):
        currSum = sum(sumParts)
        sumParts.pop(0)

        if prevSum > -1:
            if currSum > prevSum:
                count += 1
        prevSum = currSum
        currSum = 0

print(count)