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
        positions = [ int(x) for x in f.readline().strip().split(',')]
        minPos = min(positions)
        maxPos = max(positions)
        movement = [0 for x in range(minPos, maxPos+1)]
        for position in range(minPos, maxPos+1):
            for currentPos in positions:
                movement[position] += abs(currentPos - position)
        print(f'Cheapest position: {movement.index(min(movement))}')
        print(f'Cheapest Movement Cost: {min(movement)}')

@profiler
def part2():
    with open(sys.argv[1]) as f:
        positions = [ int(x) for x in f.readline().strip().split(',')]
        minPos = min(positions)
        maxPos = max(positions)
        minMovement = -1
        minPosition = -1
        for position in range(minPos, maxPos+1):
            movement = 0
            for currentPos in positions:
                distance = abs(currentPos - position)
                movement += sum(range(distance+1))
                if movement > minMovement and minMovement != -1:
                    break
            if movement < minMovement or minMovement == -1:
                minMovement = movement
                minPosition = position
            
        print(f'Cheapest position: {minPosition}')
        print(f'Cheapest Movement Cost: {minMovement}')

if __name__ == "__main__":
    part1()
    part2()