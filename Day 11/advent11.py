import sys
import time
import queue

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
    octopi = []
    flashes = 0
    for line in open(sys.argv[1], 'r'):
        octopi.append(list(map(lambda x: int(x), list(line.strip()))))

    for cycle in range(100):
        # increase
        for row in range(len(octopi)):
            octopi[row] = list(map(lambda x: x+1, octopi[row]))

        flashList = queue.SimpleQueue()
        for row in range(len(octopi)):
            for col in range(len(octopi[row])):
                if octopi[row][col] == 10:
                    flashList.put(f'{row}:{col}')
        
        flashes += flashList.qsize()

        while not flashList.empty():
            node = flashList.get()
            x, y = node.split(':')
            for row in range(int(x) -1, int(x) + 2):
                for col in range(int(y) -1, int(y) + 2):
                    if row == int(x) and col == int(y):
                        continue
                    if row < 0 or row > (len(octopi)-1) or col < 0 or col > (len(octopi[0])-1):
                        continue
                    octopi[row][col] += 1
                    if octopi[row][col] == 10:
                        flashList.put(f'{row}:{col}')
                        flashes += 1


        # reset
        for row in range(len(octopi)):
            for col in range(len(octopi[row])):
                if octopi[row][col] > 9:
                    octopi[row][col] = 0

    print(f'Final score: {flashes}')

@profiler
def part2():
    octopi = []

    for line in open(sys.argv[1], 'r'):
        octopi.append(list(map(lambda x: int(x), list(line.strip()))))

    totalOctopi = len(octopi) * len(octopi[0])

    cycles = 0
    while True:
        cycles += 1
        flashes = 0
        # increase
        for row in range(len(octopi)):
            octopi[row] = list(map(lambda x: x+1, octopi[row]))

        flashList = queue.SimpleQueue()
        for row in range(len(octopi)):
            for col in range(len(octopi[row])):
                if octopi[row][col] == 10:
                    flashList.put(f'{row}:{col}')
        
        flashes += flashList.qsize()

        while not flashList.empty():
            node = flashList.get()
            x, y = node.split(':')
            for row in range(int(x) -1, int(x) + 2):
                for col in range(int(y) -1, int(y) + 2):
                    if row == int(x) and col == int(y):
                        continue
                    if row < 0 or row > (len(octopi)-1) or col < 0 or col > (len(octopi[0])-1):
                        continue
                    octopi[row][col] += 1
                    if octopi[row][col] == 10:
                        flashList.put(f'{row}:{col}')
                        flashes += 1
        if flashes == totalOctopi:
            print(f'All flashed: {cycles}')
            break

        # reset
        for row in range(len(octopi)):
            for col in range(len(octopi[row])):
                if octopi[row][col] > 9:
                    octopi[row][col] = 0

if __name__ == "__main__":
    part1()
    part2()