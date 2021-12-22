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

def explodes(val):
    changed = False
    depth = 0
    pos = 0
    last_digit = None
    explode_right= None
    explode_pos = None
    explode_depth = None
    while pos < len(val):
        if val[pos] == '[':
            depth += 1
            if explode_right == None and depth > 4:
                if last_digit:
                    val[last_digit] = str(int(val[last_digit]) + int(val[pos+1]))
                explode_right = int(val[pos+3])
                depth -= 1
                explode_pos = pos
                explode_depth = depth
                val = val[:pos] + ['0'] + val[pos+5:]
                changed == True
        elif val[pos] == ']':
            depth -= 1
        elif val[pos].isdigit():
            if explode_right != None:
                val[pos] = str(explode_right + int(val[pos]))
                explode_right = None
                depth = explode_depth
                pos = explode_pos
            last_digit = pos
        pos += 1
    return (changed, val)

def splits(val):
    changed = False
    pos = 0
    while pos < len(val):
        if val[pos].isdigit() and int(val[pos]) > 9:
            changed = True
            num = int(val[pos])
            val = val[:pos] + ['[', str(math.floor(num/2)), ',', str(math.ceil(num/2)), ']'] + val[pos+1:]
            break
        pos += 1
    return (changed, val)

def magnitude(val):
    result = 0
    while x := re.search("\[\d+,\d+\]", val):
        nums = eval(x.group())
        result = nums[0]*3 + nums[1] * 2
        val = val[:x.span()[0]] + str(result) + val[x.span()[1]:]
    return result

@profiler
def part1():
    number = None
    changed = False
    for line in open(sys.argv[1], 'r'):
        if number:
            number = ['['] + number + [','] + list(line.strip()) + [']']
            changed = True
        else:
            number = list(line.strip())
        while changed:
            (changed, number) = explodes(number)
            (changed, number) = splits(number)
    result = magnitude(''.join(number))
    print(f'Magnitude: {result}')

@profiler
def part2():
    numbers = []
    for line in open(sys.argv[1], 'r'):
        numbers.append(line.strip())

    result = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue

            changed = True
            number = '[' + numbers[i] + ',' + numbers[j] + ']'
            number = list(number)
            while changed:
                (changed, number) = explodes(number)
                (changed, number) = splits(number)
            mag = magnitude(''.join(number))
            result = max(mag, result)
    print(f'Max Magnitude: {result}')

if __name__ == "__main__":
    part1()
    part2()