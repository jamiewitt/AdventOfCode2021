from functools import reduce
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
    heightmap = []
    for line in open(sys.argv[1], 'r'):
        heightmap.append(list(map(lambda x: int(x), list(line.strip()))))

    sum = 0
    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            if col > 0 and heightmap[row][col] >= heightmap[row][col-1]:
                continue
            if col < (len(heightmap[row]) - 1) and heightmap[row][col] >= heightmap[row][col+1]:
                continue
            if row > 0 and heightmap[row][col] >= heightmap[row-1][col]:
                continue
            if row < (len(heightmap) - 1) and heightmap[row][col] >= heightmap[row+1][col]:
                continue
            sum += (heightmap[row][col] + 1)
    print(f'Sum: {sum}')

class Graph:
    def solve(self, matrix):
      self.rowLen = len(matrix)
      self.colLen = len(matrix[0])
      islandSizes = []
      for row in range(self.rowLen):
         for col in range(self.colLen):
            if matrix[row][col] != 9:
               self.total = 0
               self.dfs(matrix, row, col)
               islandSizes.append(self.total)
      return islandSizes

    def dfs(self, matrix, row, col):
      self.total += 1
      matrix[row][col] = 9
      if row - 1 >= 0 and matrix[row - 1][col] != 9:
         self.dfs(matrix, row - 1, col)
      if col - 1 >= 0 and matrix[row][col - 1] != 9:
         self.dfs(matrix, row, col - 1)
      if row + 1 < self.rowLen and matrix[row + 1][col] != 9:
         self.dfs(matrix, row + 1, col)
      if col + 1 < self.colLen and matrix[row][col + 1] != 9:
         self.dfs(matrix, row, col + 1)

@profiler
def part2():

    heightmap = []
    for line in open(sys.argv[1], 'r'):
        heightmap.append(list(map(lambda x: int(x), list(line.strip()))))

    basinsizes = Graph().solve(heightmap)
    total = reduce(lambda x,y: x*y, sorted(basinsizes)[-3:])
    print(f'Total: {total}')


if __name__ == "__main__":
    part1()
    part2()