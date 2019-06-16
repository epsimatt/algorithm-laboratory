from typing import List


# runtime: 99.77%, memory usage: 44.79%
def singleNumber(nums: 'List[int]') -> 'int':
    result = 0

    for n in nums:
        result ^= n

    return result


if __name__ == '__main__':
    result = singleNumber([4, 1, 2, 1, 2])

    print(result)