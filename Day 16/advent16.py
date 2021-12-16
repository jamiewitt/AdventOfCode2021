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

def hex2binary(val):
    return bin(int(val, 16))[2:].zfill(len(val)*4)

def process_instruction(bin_instruction):
    results = []    
    ver = int(bin_instruction[:3], 2)
    id = int(bin_instruction[3:6], 2)
    bin_instruction = bin_instruction[6:]
    if id == 4:
        digits = ''
        while bin_instruction[0] == '1':
            digits += bin_instruction[1:5]
            bin_instruction = bin_instruction[5:]
        digits += bin_instruction[1:5]
        bin_instruction = bin_instruction[5:]
        results.append((ver, id, int(digits, 2)))
    else:
        operator_results = []
        len_type_id = bin_instruction[0]
        bin_instruction = bin_instruction[1:]
        if len_type_id == '0':
            num_bit_length = int(bin_instruction[:15], 2)
            bin_instruction = bin_instruction[15:]
            sub_packets = bin_instruction[:num_bit_length]
            bin_instruction = bin_instruction[num_bit_length:]
            while len(sub_packets) > 0 and int(sub_packets) != 0:
                sub_results, sub_packets = process_instruction(sub_packets)
                operator_results += sub_results
        else:
            num_sub_packages= int(bin_instruction[:11], 2)
            bin_instruction = bin_instruction[11:]
            for x in range(num_sub_packages):
                sub_results, bin_instruction = process_instruction(bin_instruction)
                operator_results += sub_results
    
        results.append((ver, id, operator_results))
    return (results, bin_instruction)

def version_total(result):
    total = result[0]
    if type(result[2]) == type([]):
        for sub_result in result[2]:
            total += version_total(sub_result)
    return total

@profiler
def part1():
    instructions = []
    for line in open(sys.argv[1], 'r'):
        instructions.append(line.strip())

    for instruction in instructions:
        ver_total = 0
        bin_instruction = hex2binary(instruction)
        while len(bin_instruction) > 0 and int(bin_instruction) != 0:
            results, bin_instruction= process_instruction(bin_instruction)
            for result in results:
                ver_total += version_total(result)
        print(f'Version Total: {ver_total}')

def calc_score(result):
    if result[1] == 0:
        nums = []
        for sub_result in result[2]:
            nums.append(calc_score(sub_result))
        return reduce(lambda x,y: x+y, nums)
    elif result[1] == 1:
        nums = []
        for sub_result in result[2]:
            nums.append(calc_score(sub_result))
        return reduce(lambda x,y: x*y, nums)
    elif result[1] == 2:
        nums = []
        for sub_result in result[2]:
            nums.append(calc_score(sub_result))
        return min(nums)
    elif result[1] == 3:
        nums = []
        for sub_result in result[2]:
            nums.append(calc_score(sub_result))
        return max(nums)
    elif result[1] == 4:
        return result[2]
    elif result[1] == 5:
        nums = []
        for sub_result in result[2]:
            nums.append(calc_score(sub_result))
        return int(nums[0] > nums[1])
    elif result[1] == 6:
        nums = []
        for sub_result in result[2]:
            nums.append(calc_score(sub_result))
        return int(nums[0] < nums[1])
    elif result[1] == 7:
        nums = []
        for sub_result in result[2]:
            nums.append(calc_score(sub_result))
        return int(nums[0] == nums[1])
    else:
        raise Exception('Unknown operation')

@profiler
def part2():
    instructions = []
    for line in open(sys.argv[1], 'r'):
        instructions.append(line.strip())

    for instruction in instructions:
        bin_instruction = hex2binary(instruction)
        while len(bin_instruction) > 0 and int(bin_instruction) != 0:
            results, bin_instruction= process_instruction(bin_instruction)
            for result in results:
                print(f'Result: {calc_score(result)}')

if __name__ == "__main__":
    part1()
    part2()