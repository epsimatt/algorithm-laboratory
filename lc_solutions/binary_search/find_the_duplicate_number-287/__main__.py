from typing import List


# runtime: 40.90%, memory usage: 26.17%
def findDuplicate_v1(nums: List[int]) -> int:
    values = sorted(nums)

    low = 0
    high = len(values) - 1

    low_current = 0
    high_current = 0

    if high == 1:
        return values[0]
    else:
        while low <= high:
            if low > 0 and low_current == values[low]:
                return low_current
            else:
                low_current = values[low]

            if high < len(values) - 1 and high_current == values[high]:
                return high_current
            else:
                high_current = values[high]

            low += 1
            high -= 1

        return -1


# runtime: 54.54%, memory usage: 30.81%
def findDuplicate_v2(nums: List[int]) -> int:
    values = sorted(nums)

    low = 0
    high = len(values) - 1

    if high == 1:
        return values[0]
    else:
        while low <= high:
            if values[low] == values[low + 1]:
                return values[low]

            if values[high] == values[high - 1]:
                return values[high]

            low += 1
            high -= 1

        return -1


if __name__ == '__main__':
    print(findDuplicate_v2([1, 1])) # 1
    print(findDuplicate_v2([1, 3, 4, 2, 1]))  # 1
    print(findDuplicate_v2([1, 3, 4, 2, 2])) # 2
    print(findDuplicate_v2([3, 1, 3, 4, 2])) # 3