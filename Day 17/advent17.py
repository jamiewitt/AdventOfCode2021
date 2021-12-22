import sys
import time
import math
import re

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
    for line in open(sys.argv[1], 'r'):
        x, y = line.strip().split(':')[1].split(',')
        x = [int(i) for i in x.split('=')[1].split('..')]
        y = [int(i) for i in y.split('=')[1].split('..')]
    
    y_min = min(y)
    y_max = max(y)
    distances = [sum(range(i)) for i in range(1, x[0]+1)]

    x_min = min(x)
    x_max = max(x)
    x_velocity_min = len(list(filter(lambda i: i<x[0], distances)))

    max_y = sys.maxsize * -1
    for i in range(x_velocity_min, x_max):
        starting_y_velocity = 0
        overshot = False
        while not overshot:
            pos = [0,0]
            y_velocity = starting_y_velocity
            if y_velocity > max(abs(y_min), abs(y_max)):
                break
            highest = 0
            x_velocity = i
            while pos[0] < x_max:
                pos[0] += x_velocity
                pos[1] += y_velocity
                highest = max(highest, pos[1])
                y_velocity -= 1
                x_velocity = x_velocity if x_velocity == 0 else x_velocity - 1
                if pos[0] > x_max and pos[1] > y_max:
                    overshot = True
                if pos[1] < y_min:
                    break
                if x_min <= pos[0] <= x_max and y_min <= pos[1] <= y_max:
                    max_y = max(max_y, highest) if highest != None else max_y
                    break
            if overshot:
                break
            starting_y_velocity += 1
    print(f'Max Y: {max_y}')

@profiler
def part2():
    answer_set = []
    for line in open('answer.txt', 'r'):
        answer_set += line.strip().split()
    for line in open(sys.argv[1], 'r'):
        x, y = line.strip().split(':')[1].split(',')
        x = [int(i) for i in x.split('=')[1].split('..')]
        y = [int(i) for i in y.split('=')[1].split('..')]
    
    y_min = min(y)
    y_max = max(y)
    distances = [sum(range(i)) for i in range(1, x[0]+1)]

    x_min = min(x)
    x_max = max(x)
    x_velocity_min = len(list(filter(lambda i: i<x[0], distances)))

    max_y = sys.maxsize * -1
    valids = []
    for i in range(x_velocity_min, x_max+1):
        starting_y_velocity = y_min
        overshot = False
        while not overshot:
            pos = [0,0]
            y_velocity = starting_y_velocity
            if y_velocity > max(abs(y_min), abs(y_max)):
                break
            highest = 0
            x_velocity = i
            while pos[0] < x_max:
                pos[0] += x_velocity
                pos[1] += y_velocity
                highest = max(highest, pos[1])
                y_velocity -= 1
                x_velocity = x_velocity if x_velocity == 0 else x_velocity - 1
                if pos[0] > x_max and pos[1] > y_max:
                    overshot = True
                if pos[1] < y_min:
                    break
                if x_min <= pos[0] <= x_max and y_min <= pos[1] <= y_max:
                    max_y = max(max_y, highest) if highest != None else max_y
                    valids.append(f'{i},{starting_y_velocity}')
                    break
            if overshot:
                break
            starting_y_velocity += 1
    print(f'Valid velocities: {len(valids)}')

if __name__ == "__main__":
    part1()
    part2()