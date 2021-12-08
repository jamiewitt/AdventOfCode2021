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
    count = 0
    for line in open(sys.argv[1], 'r'):
        codes, output = line.strip().split('|')
        for code in output.split():
            if (len(code) in [2, 3, 4, 7]):
                count +=1
    print(f'1478s: {count}')

@profiler
def part2():
    total = 0
    for line in open(sys.argv[1], 'r'):
        codes, output = line.strip().split('|')
        digit_key = ['' for x in range(10)]
        final_code = output.split()
        unknowns = sorted(codes.split() + output.split(), key=lambda el: len(el))
        current_pos = 0
        while len(unknowns) > 0:
            current_code = "".join(sorted(unknowns[current_pos]))
            if (len(current_code) == 2):
                # 1
                digit_key[1] = current_code
                del unknowns[current_pos]
            elif (len(current_code) == 4):
                # 4
                digit_key[4] = current_code
                del unknowns[current_pos]
            elif (len(current_code) == 3):
                # 7
                digit_key[7] = current_code
                del unknowns[current_pos]
            elif (len(current_code) == 7):
                # 8
                digit_key[8] = current_code
                del unknowns[current_pos]
            elif (len(current_code) == 5):
                # 2, 3, 5
                matches = 0
                if (digit_key[1] != ''):
                    matches = len(set(current_code).intersection(digit_key[1]))
                elif (digit_key[7] != ''):
                    matches = len(set(current_code).intersection(digit_key[7])) - 1
                else:
                    current_pos +=1
                    continue
                if (matches == 2):
                    # 3
                    digit_key[3] = current_code
                    del unknowns[current_pos]
                elif (matches == 1):
                    # 2, 5
                    if (digit_key[4] != ''):
                        matches = len(set(current_code).intersection(digit_key[4]))
                        if (matches == 3):
                            digit_key[5] = current_code
                            del unknowns[current_pos]
                        if (matches == 2):
                            digit_key[2] = current_code
                            del unknowns[current_pos]
                    else:
                        current_pos += 1
                        continue
            elif (len(current_code) == 6):
                # 0, 6, 9
                matches = 0
                if (digit_key[1] != ''):
                    matches = len(set(current_code).intersection(digit_key[1]))
                elif (digit_key[7] != ''):
                    matches = len(set(current_code).intersection(digit_key[7])) - 1
                else:
                    current_pos +=1
                    continue
                if (matches == 1):
                    # 6
                    digit_key[6] = current_code
                    del unknowns[current_pos]
                elif (matches == 2):
                    # 0, 9
                    if (digit_key[4] != ''):
                        matches = len(set(current_code).intersection(digit_key[4]))
                        if (matches == 4):
                            digit_key[9] = current_code
                            del unknowns[current_pos]
                        elif (matches == 3):
                            digit_key[0] = current_code
                            del unknowns[current_pos]
                        else:
                            current_pos += 1
                            continue
                    else:
                        current_pos != 1
                        continue

        final_code_decoded = ''
        for code in final_code:
            code = "".join(sorted(code))
            if code in digit_key:
                final_code_decoded += str(digit_key.index(code))
            else:
                raise Exception(f'Code: {code}')
        total += int(final_code_decoded)
    print(f'Total: {total}')

if __name__ == "__main__":
    part1()
    part2()