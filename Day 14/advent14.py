import sys
import time
from collections import defaultdict
import copy
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
    polymer = []
    rules = {}
    rules_section = False
    for line in open(sys.argv[1], 'r'):
        if line.strip() == '':
            rules_section = True
            continue
        if rules_section:
            code, element = line.strip().split(' -> ')
            rules[code] = element
        else:
            polymer = list(line.strip())
    
    for i in range(10):
        new_polymer = [polymer[0]]
        for j in range(len(polymer)-1):
            new_polymer += [rules[polymer[j] + polymer[j+1]], polymer[j+1]]
        polymer = new_polymer.copy()

    elements = set(polymer)
    element_counts = []
    for element in elements:
        element_counts.append(polymer.count(element))
    element_counts.sort()
    print(f'Result: {element_counts[-1] - element_counts[0]}')

@profiler
def part2():
    polymer = defaultdict(lambda: defaultdict(lambda: 0))
    rules = {}
    last_element = ''
    rules_section = False
    for line in open(sys.argv[1], 'r'):
        if line.strip() == '':
            rules_section = True
            continue
        if rules_section:
            code, element = line.strip().split(' -> ')
            rules[code] = element
        else:
            element_list = list(line.strip())
            last_element = element_list[-1]
            for i in range(len(element_list)-1):
                polymer[element_list[i]][element_list[i+1]] = 1

    for i in range(40):
        new_polymer = defaultdict(lambda: defaultdict(lambda: 0))
        for element in polymer.keys():
            for adj_element in polymer[element].keys():
                new_element = rules[element + adj_element]
                new_polymer[element][new_element] += polymer[element][adj_element]
                new_polymer[new_element][adj_element] += polymer[element][adj_element]
        polymer = new_polymer

    element_counts = []
    for element in polymer.keys():
        count = reduce(lambda x, y: x+y, polymer[element].values())
        if element == last_element:
            count += 1
        element_counts.append(count)
    element_counts.sort()
    print(f'Result: {element_counts[-1] - element_counts[0]}')

if __name__ == "__main__":
    part1()
    part2()