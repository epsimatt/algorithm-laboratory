from typing import List


# runtime: 63.30%, memory usage: 5.53%
def searchInsert(nums: List[int], target: int) -> int:
    n = len(nums)
    low, high = 0, n - 1

    while low < high:
        pivot = int((low + high) / 2)

        if nums[pivot] == target:
            return pivot
        elif nums[pivot] < target:
            low = pivot + 1
        else:
            high = pivot - 1

    if target > nums[low]:
        return low + 1
    else:
        return low


if __name__ == '__main__':
    print(searchInsert([1, 3, 5, 6], 5)) # 2
    print(searchInsert([1, 3, 5, 6], 2)) # 1
    print(searchInsert([1, 3, 5, 6], 7)) # 4
    print(searchInsert([1, 3, 5, 6], 0)) # 0