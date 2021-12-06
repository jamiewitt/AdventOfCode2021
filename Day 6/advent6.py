import sys
import time
from functools import reduce

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
    with open(sys.argv[1]) as f:
        fishes = [ int(x) for x in f.readline().strip().split(',')]

        for day in range(80):
            new_fish = []
            for fishNum in range(len(fishes)):
                fishes[fishNum] -= 1
                if fishes[fishNum] == -1:
                    fishes[fishNum] = 6
                    new_fish.append(8)
            fishes += new_fish
        print(f'Total fish: {len(fishes)}')

@profiler
def part2():
    with open(sys.argv[1]) as f:
        initial_fishes = [ int(x) for x in f.readline().strip().split(',')]
        fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for fish in initial_fishes:
            fishes[fish] += 1

        for day in range(256):
            new_fish = fishes[0]
            for fishNum in range(len(fishes)-1):
                fishes[fishNum] = fishes[fishNum+1]
            fishes[8] = new_fish
            fishes[6] += new_fish

        print(f'Total fish: {reduce(lambda x, y: x+y, fishes)}')
if __name__ == "__main__":
    part1()
    part2()