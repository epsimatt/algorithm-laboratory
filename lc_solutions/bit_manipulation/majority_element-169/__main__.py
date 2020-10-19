from typing import List


# runtime: 99.51%, memory usage: 31.35%
def majorityElement(nums: 'List[int]') -> 'int':
    max_count = [0, 0]

    for n in set(nums):
        if nums.count(n) > max_count[1]:
            max_count[0] = n
            max_count[1] = nums.count(n)

    return max_count[0]


if __name__ == '__main__':
    result = majorityElement([2, 2, 1, 1, 1, 2, 2])

    print(result)