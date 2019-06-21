from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    low = 0
    high = len(numbers) - 1

    while low < high:
        if numbers[low] + numbers[high] < target:
            low += 1
        elif numbers[low] + numbers[high] > target:
            high -= 1
        else:
            return [low + 1, high + 1]


if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([2, 7, 11, 15], 13))
    print(twoSum([2, 7, 11, 15], 17))
    print(twoSum([2, 7, 11, 15], 18))
    print(twoSum([2, 7, 11, 15], 22))
    print(twoSum([2, 7, 11, 15], 26))