import sys
import time
from collections import defaultdict

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
    coordinates = defaultdict(int)
    for line in open(sys.argv[1], 'r'):
        [start, end] = line.strip().split(' -> ')
        [x1, y1] = start.split(',')
        [x2, y2] = end.split(',')

        # horizontal line
        if y1 == y2:
            for x in range(min(int(x1),int(x2)), max(int(x1),int(x2))+1):
                curr = str(x) + ',' + y1
                coordinates[curr] += 1
        # vertical line
        elif x1 == x2:
            for y in range(min(int(y1),int(y2)), max(int(y1),int(y2))+1):
                curr = x1 + ',' + str(y)
                coordinates[curr] += 1

    dangers = 0
    for key in coordinates.keys():
        if coordinates[key] > 1:
            dangers += 1

    print (f'Dangers: {dangers}')

@profiler
def part2():
    coordinates = defaultdict(int)
    for line in open(sys.argv[1], 'r'):
        [start, end] = line.strip().split(' -> ')
        [x1, y1] = start.split(',')
        [x2, y2] = end.split(',')

        # horizontal line
        if y1 == y2:
            for x in range(min(int(x1),int(x2)), max(int(x1),int(x2))+1):
                curr = str(x) + ',' + y1
                coordinates[curr] += 1
        # vertical line
        elif x1 == x2:
            for y in range(min(int(y1),int(y2)), max(int(y1),int(y2))+1):
                curr = x1 + ',' + str(y)
                coordinates[curr] += 1
        # diagonal
        else:
            if (int(x1) < int(x2)):
                xRange = range(int(x1), int(x2)+1)
            else:
                xRange = range(int(x1), int(x2)-1, -1)

            if (int(y1) < int(y2)):
                yRange = range(int(y1), int(y2)+1)
            else:
                yRange = range(int(y1), int(y2)-1, -1)

            for x,y in zip(xRange, yRange):
                curr = str(x) + ',' + str(y)
                coordinates[curr] += 1

    dangers = 0
    for key in coordinates.keys():
        if coordinates[key] > 1:
            dangers += 1

    print (f'Dangers: {dangers}')

if __name__ == "__main__":
    part1()
    part2()