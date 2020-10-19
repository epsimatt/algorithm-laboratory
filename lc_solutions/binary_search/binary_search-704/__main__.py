from typing import List


# runtime: 72.14%, memory usage: 23.88%
def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums)

    while low < high:
        pivot = int((low + high) / 2)

        if nums[pivot] == target:
            return pivot
        elif nums[pivot] < target:
            low = pivot + 1
        else:
            high = pivot

    return -1


if __name__ == '__main__':
    print(search([-1, 0, 3, 5, 9, 12], 9)) # 4
    print(search([-1, 0, 3, 5, 9, 12], 2)) # -1