import sys
import time
import numpy as np

def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' +
              "{:2.5f}".format(time.time()-t) + ' sec')
        return ret
    return wrapper_method

@profiler
def part1():
    pos = []
    scores = [0, 0]
    for line in open(sys.argv[1], 'r'):
        pos.append(int(line.strip().split()[-1]))

    die = 1
    turn = 0
    total_rolls = 0
    while max(scores) < 1000:
        rolls = sum(range(die, die+3))
        die = (die + 3) % 100
        pos[turn] = (pos[turn] + rolls) % 10 if (pos[turn] + rolls) % 10 else 10
        scores[turn] += pos[turn]
        turn = (turn + 1) % 2
        total_rolls += 3
    print(f'Result: {scores[turn] * total_rolls}')

def take_turn(input_scores, input_positions, rolls, indent = ""):
    wins = [0, 0]
    for r in set(rolls):
        player_1_position = (input_positions[0] + r) % 10
        player_1_position = player_1_position if player_1_position != 0 else 10
        player_1_score = input_scores[0] + player_1_position
        if player_1_score >= 21:
            wins[0] += rolls.count(r)
            continue

        for s in set(rolls):
            player_2_position = (input_positions[1] + s) % 10
            player_2_position = player_2_position if player_2_position != 0 else 10
            player_2_score = input_scores[1] + player_2_position
            factor = rolls.count(r) * rolls.count(s)
            if player_2_score >= 21:
                wins[1] += factor
                continue
            sub_wins = take_turn([player_1_score, player_2_score], [player_1_position, player_2_position], rolls, indent + "==")
            wins[0] += (sub_wins[0] * factor)
            wins[1] += (sub_wins[1] * factor)
    return wins


@profiler
def part2():
    original_pos = []
    for line in open(sys.argv[1], 'r'):
        original_pos.append(int(line.strip().split()[-1]))

    rolls = []
    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            for k in [1, 2, 3]:
                rolls.append(i+j+k)

    wins = take_turn([0,0], original_pos, rolls)
    print(f'Result: {wins}')
    print(f'Most wins {max(wins)}')

if __name__ == "__main__":
    part1()
    part2()
