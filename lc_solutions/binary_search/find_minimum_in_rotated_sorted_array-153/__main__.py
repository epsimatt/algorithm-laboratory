from typing import List

import sys


# runtime: 72.48%, memory usage: 6.00%
def findMin(nums: List[int]) -> int:
    n, result = len(nums), sys.maxsize

    low, high = 0, n - 1

    while low <= high:
        piv = (low + high) // 2

        if result > nums[piv]:
            result = nums[piv]
        else:
            if nums[piv] > nums[high]:
                low = piv + 1
            else:
                high = piv - 1

    return result


if __name__ == '__main__':
    print(findMin([3, 4, 5, 1, 2])) # 1
    print(findMin([4, 5, 6, 7, 0, 1, 2])) # 0
