from functools import reduce

file1 = open('input.txt', 'r')

lines = file1.readlines()
called_numbers = lines[0].strip().split(',')

board = 0
used_numbers = {}
boards = {}
boards[0] = []

for i in range(2, len(lines)):
    line = lines[i].strip()
    if (line == ''):
        board += 1
        boards[board] = []
        continue

    for num in line.split():
        if (not num in used_numbers):
            used_numbers[num] = []
        used_numbers[num].append(board)
        boards[board].append(num)

def checkRows(board):
    for row_num in range(5):
        row_start = row_num*5
        row_end = row_start+5
        row = board[row_start:row_end]
        if (reduce(lambda x, y: int(x)+int(y), row) == -5):
            return True
    return False

def checkColumns(board):
    for col_num in range(5):
        col_start = col_num
        col_end = len(board)
        col = board[col_start:col_end:5]
        if (reduce(lambda x, y: int(x)+int(y), col) == -5):
            return True
    return False

class Winner(Exception):
    pass

winners = []
board_numbers = list(boards.keys())
final_number = 0
latest_winner = ''

try:
    for called_number in called_numbers:
        final_number = int(called_number)
        for board in used_numbers[called_number]:
            boards[board][boards[board].index(called_number)] = -1
            if checkRows(boards[board]):
                winners.append(board)
                latest_winner = board
                if board in board_numbers:
                    board_numbers.remove(board)
                # raise Winner(board)
            if checkColumns(boards[board]):
                winners.append(board)
                latest_winner = board
                if board in board_numbers:
                    board_numbers.remove(board)
                # raise Winner(board)
            if (len(board_numbers) == 0):
                raise Winner(latest_winner)
except Winner as e:
    print(f'Winner Board: {e}')

sum = 0
for num in boards[latest_winner]:
    if (num != -1):
        sum += int(num)
print(f'Sum: {sum}')
print(f'Final Score: {sum*final_number}')
