from typing import List


# runtime: 21.81%, memory usage: 52.82%
def twoSum_v1(nums: List[int], target: int) -> List[int]:
    # 첫 번째 숫자 선택
    for i, v in enumerate(nums):
        # 두 번째 숫자 선택
        for j, w in enumerate(nums[i + 1:]):
            if v + w == target:
                return [i, i + j + 1]


# runtime: 20.48%, memory usage: 93.96%
def twoSum_v2(nums: List[int], target: int) -> List[int]:
    n = len(nums)

    for i in range(0, n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


# runtime: 97.81%, memory usage: 29.44%
def twoSum_v3(nums: List[int], target: int) -> List[int]:
    values = sorted(nums)
    indexes = sorted(range(len(nums)), key=lambda i: nums[i])

    low = 0
    high = len(values) - 1

    while low < high:
        if values[low] + values[high] == target:
            return [indexes[low], indexes[high]]
        elif values[low] + values[high] > target:
            high -= 1
        else:
            low += 1

    return [-1, -1]


# runtime: 97.65%, memory usage: 12.50%
def twoSum_v4(nums: List[int], target: int) -> List[int]:
    values = sorted(zip(nums, range(len(nums))))

    low = 0
    high = len(values) - 1

    while low < high:
        if values[low][0] + values[high][0] == target:
            return [values[low][1], values[high][1]]
        elif values[low][0] + values[high][0] > target:
            high -= 1
        else:
            low += 1

    return [-1, -1]


if __name__ == '__main__':
    print(twoSum_v4([2, 7, 11, 15], 9)) # [0, 1]
    print(twoSum_v4([3, 3], 6)) # [0, 1]
    print(twoSum_v4([3, 2, 4], 6))  # [1, 2]
    print(twoSum_v4([3, 2, 3], 6))  # [0, 2]