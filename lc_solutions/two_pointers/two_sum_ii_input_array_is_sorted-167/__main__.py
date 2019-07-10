from typing import List


# runtime: 93.20%, memory usage: 24.67%
def twoSum_v1(numbers: List[int], target: int) -> List[int]:
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
    result = twoSum_v1([2, 7, 11, 15], 9)
    print(result)