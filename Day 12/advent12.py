import sys
import time

def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' +
              "{:2.5f}".format(time.time()-t) + ' sec')
        return ret
    return wrapper_method

def wander(map, start, end, visited = set(), path = []):
    result = []
    path.append(start)
    if start == end:
        return [','.join(path)]
        
    if start.upper() != start:
        visited.add(start)

    for adj in map[start]:
        if (adj in visited):
            continue
        result += wander(map, adj, end, visited.copy(), path[:])
    
    return result


@profiler
def part1():
    caveMap = {}
    for line in open(sys.argv[1], 'r'):
        x, y = line.strip().split('-')
        if not x in caveMap.keys():
            caveMap[x] = []
        caveMap[x].append(y)
        if not y in caveMap.keys():
            caveMap[y] = []
        caveMap[y].append(x)
        
    paths = wander(caveMap, 'start', 'end')
    print(f'Paths: {len(paths)}')


def wander2(map, start, end, visited = set(), path = [], revisit_used = 0):
    result = []
    path.append(start)
    if start == end:
        return [','.join(path)]
        
    if start.upper() != start:
        visited.add(start)

    for adj in map[start]:
        revisit = revisit_used
        if adj in visited:
            if revisit_used == 1 or adj == 'start':
                continue
            revisit = 1
        result += wander2(map, adj, end, visited.copy(), path[:], revisit)
    
    return result


@profiler
def part2():
    caveMap = {}
    for line in open(sys.argv[1], 'r'):
        x, y = line.strip().split('-')
        if not x in caveMap.keys():
            caveMap[x] = []
        caveMap[x].append(y)
        if not y in caveMap.keys():
            caveMap[y] = []
        caveMap[y].append(x)
        
    paths = wander2(caveMap, 'start', 'end')
    print(f'Paths: {len(paths)}')

if __name__ == "__main__":
    part1()
    part2()