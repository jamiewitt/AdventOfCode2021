from collections import defaultdict
import sys
import time
from functools import reduce
from math import dist, inf

def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' +
              "{:2.5f}".format(time.time()-t) + ' sec')
        return ret
    return wrapper_method

def listToCoordinate(val):
    return str(val[0]) + ',' + str(val[1])

def coordinatesToList(val):
    return [int(i) for i in val.split(',')]

@profiler
def part1():
    cave_map = []
    distances = []
    for line in open(sys.argv[1], 'r'):
        cave_map.append([int(x) for x in list(line.strip())])
        distances.append([sys.maxsize for x in list(line.strip())])

    start = '0,0'

    shortest = defaultdict(list)
    shortest[0] = ['0,0']
    distances[0][0] = 0
    node = start

    while shortest:
        current_distance = min(shortest.keys())
        nodes = shortest[current_distance]
        shortest.pop(current_distance)

        for node in nodes:
            [x,y] = coordinatesToList(node)

            neighbors = []
            for i in range(x-1, x+2):
                if i >= 0 and i < len(cave_map[0]) and i != x:
                    neighbors.append([i, y])
            for j in range(y-1, y+2):
                if j >= 0 and j < len(cave_map) and j != y:
                    neighbors.append([x, j])
            for neighbor in neighbors:
                neighbor_distance = current_distance + cave_map[neighbor[1]][neighbor[0]]
                if neighbor_distance < distances[neighbor[1]][neighbor[0]]:
                    distances[neighbor[1]][neighbor[0]] = neighbor_distance
                    shortest[neighbor_distance].append(listToCoordinate(neighbor))
        
    print(f'Least risk: {distances[len(cave_map)-1][len(cave_map[0])-1]}')

@profiler
def part2():
    cave_map = []
    distances = []
    for line in open(sys.argv[1], 'r'):
        row = [int(x) for x in list(line.strip())]
        cave_map.append(row)
    tile_size = len(cave_map)

    rows = tile_size * 5
    cols = tile_size * 5

    def get_cavemap(row, col):
        x = (cave_map[row % tile_size][col % tile_size] + (row // tile_size) + (col // tile_size))
        return (x - 1) % 9 + 1

    distances = [[sys.maxsize for x in range(tile_size * 5)] for y in range(tile_size * 5)]
    start = '0,0'

    shortest = defaultdict(list)
    shortest[0] = ['0,0']
    distances[0][0] = 0
    node = start

    while shortest:
        current_distance = min(shortest.keys())
        nodes = shortest[current_distance]
        shortest.pop(current_distance)

        for node in nodes:
            [x,y] = coordinatesToList(node)

            neighbors = []
            for i in range(x-1, x+2):
                if i >= 0 and i < cols and i != x:
                    neighbors.append([i, y])
            for j in range(y-1, y+2):
                if j >= 0 and j < rows and j != y:
                    neighbors.append([x, j])
            for neighbor in neighbors:
                neighbor_distance = current_distance + get_cavemap(neighbor[1], neighbor[0])
                if neighbor_distance < distances[neighbor[1]][neighbor[0]]:
                    distances[neighbor[1]][neighbor[0]] = neighbor_distance
                    shortest[neighbor_distance].append(listToCoordinate(neighbor))
    print(f'Least risk: {distances[rows-1][cols-1]}')

if __name__ == "__main__":
    part1()
    part2()