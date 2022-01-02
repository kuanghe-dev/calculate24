from collections import defaultdict
from itertools import permutations
from functools import lru_cache
# from pprint import pprint

@lru_cache(maxsize=None)
def dp(nums, beg, end):
    """Given an array 'nums', and indices 'beg' and 'end' (inclusive),
    calculate possible results nums[beg..end] can formulate with the following
    operations: addition, subtraction, multiplication, division, and parentheses.

    Return a dict. The key is possble results, and its corresponding value is
    formula(e) that lead to that specific results.
    """

    if beg == end:
        return {nums[beg]: [nums[beg]]}
    
    res = defaultdict(list)
    for mid in range(beg, end):
        for x, formulaeX in dp(nums, beg, mid).items():
            for y, formulaeY in dp(nums, mid+1, end).items():
                for fx in formulaeX:
                    # No need to put an integer in parantheses 
                    if isinstance(fx, str):
                        fx = f'({fx})'
                    for fy in formulaeY:
                        if isinstance(fy, str):
                            fy = f'({fy})'
                        res[x + y].append(f"{fx} + {fy}")
                        res[x - y].append(f"{fx} - {fy}")
                        res[x * y].append(f"{fx} * {fy}")
                        if y:
                            res[x / y].append(f"{fx} / {fy}")
    return res

class Calculate24:
    EPS = 1e-5

    def __init__(self, cards):
        self.cards = cards

    def run(self):
        for nums in set(permutations(self.cards)):
            resultDict = dp(nums,  0, 3)
            for result in resultDict:
                if abs(result - 24) < Calculate24.EPS:
                    return resultDict[result]
        return []

if __name__ == '__main__':
    inputs = [
        [5, 5, 5, 1],
        [1, 3, 4, 6],
        [1, 3, 5, 6],
        [3, 3, 4, 8],
        [6, 5, 3, 3],
        [9, 7, 8, 5],
        [9, 9, 9, 9],
        [5, 5, 5, 5],
    ]

    for input in inputs:
        print(input, '-->', Calculate24(input).run())
