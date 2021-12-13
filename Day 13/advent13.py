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

@profiler
def part1():
    dots = set()
    instructions = []
    instructionsSection = False
    for line in open(sys.argv[1], 'r'):
        if line.strip() == '':
            instructionsSection = True
            continue
        if instructionsSection:
            instructions.append(line.strip())
        else:
            dots.add(line.strip())
    dir, row = instructions[0].split()[-1].split('=')

    new_dots = set()
    for dot in dots:
        x,y = dot.split(',')
        if dir == 'x':
            if int(x) > int(row):
                new_x = int(row)- (int(x)-int(row))
                new_dots.add(f'{new_x},{y}')
            else:
                new_dots.add(dot)
        else:
            if int(y) > int(row):
                new_y = int(row)- (int(y)-int(row))
                new_dots.add(f'{x},{new_y}')
            else:
                new_dots.add(dot)

    dots = new_dots
    print(f'Dots: {len(set(dots))}')


@profiler
def part2():
    dots = set()
    instructions = []
    instructionsSection = False
    for line in open(sys.argv[1], 'r'):
        if line.strip() == '':
            instructionsSection = True
            continue
        if instructionsSection:
            instructions.append(line.strip())
        else:
            dots.add(line.strip())

    max_x = 0
    max_y = 0
    for instruction in instructions:
        dir, row = instruction.split()[-1].split('=')
        new_dots = set()
        for dot in dots:
            x,y = dot.split(',')
            if dir == 'x':
                max_x = int(row)
                if int(x) > int(row):
                    new_x = int(row)- (int(x)-int(row))
                    new_dots.add(f'{new_x},{y}')
                else:
                    new_dots.add(dot)
            else:
                max_y = int(row)
                if int(y) > int(row):
                    new_y = int(row)- (int(y)-int(row))
                    new_dots.add(f'{x},{new_y}')
                else:
                    new_dots.add(dot)

        dots = new_dots

    for y in range(max_y):
        for x in range(max_x):
            c = str(x) + ',' + str(y)
            if c in dots:
                print('#', end = '')
            else:
                print(' ', end = '')
        print('')

if __name__ == "__main__":
    part1()
    part2()