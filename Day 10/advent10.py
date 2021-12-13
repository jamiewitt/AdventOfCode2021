from functools import reduce
import sys
import time
from statistics import median


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' +
              "{:2.5f}".format(time.time()-t) + ' sec')
        return ret
    return wrapper_method

scoreKey = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
scoreKey2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
pairs = {
    '(':')',
    '[': ']',
    '{': '}',
    '<': '>'
}

def findMatch(lst, ch):
    while lst[0] in pairs.keys():
        lst = findMatch(lst[1:], lst[0])

    if lst[0] == pairs[ch]:
        return lst[1:]
    else:
        raise Exception(lst[0])

class MatchException(Exception):
    pass

def findMatch2(lst, ch):
    # print(f'{ch} List: {lst}')
    while lst[0] in pairs.keys():
        # print('recur')
        try:
            lst = findMatch2(lst[1:], lst[0])
        except IndexError as e:
            raise MatchException(f'{pairs[lst[0]]}')
        except MatchException as e:
            raise MatchException(f'{str(e)}{pairs[lst[0]]}')
  

    if lst[0] == pairs[ch]:
        # print('match')
        return lst[1:]
    else:
        raise Exception(lst[0])

@profiler
def part1():
    score = 0
    for line in open(sys.argv[1], 'r'):
        try:
            line_pieces = list(line.strip())
            while len(line_pieces) > 0:
                line_pieces = findMatch(line_pieces[1:], line_pieces[0])
        except IndexError as e:
            pass
        except Exception as e:
            # print(f'Illegal char: {str(e)}')
            score += scoreKey[str(e)]
    print(f'Final score: {score}')

@profiler
def part2():
    scores = []
    for line in open(sys.argv[1], 'r'):
        try:
            line_pieces = list(line.strip())
            while len(line_pieces) > 0:
                try:
                    line_pieces = findMatch2(line_pieces[1:], line_pieces[0])
                except MatchException as e:
                    raise MatchException(f'{str(e)}{pairs[line_pieces[0]]}')

        except MatchException as e:
            score = 0
            for ch in list(str(e)):
                score = (score * 5) + scoreKey2[ch]
            # print(f'Score: {score}')
            scores.append(score)
        except Exception as e:
            pass
    print(f'Final score: {median(scores)}')




if __name__ == "__main__":
    part1()
    part2()