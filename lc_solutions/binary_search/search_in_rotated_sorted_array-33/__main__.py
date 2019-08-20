from typing import List


# runtime: 78.32%, memory usage: 6.29%
def search(nums: List[int], target: int) -> int:
    n = len(nums)

    if n:
        low, high = 0, n - 1

        while low <= high:
            """
            [4, 5, 6, 7, 0, 1, 2],
            [6, 7, 0, 1, 2, 4, 5],
            [0, 1, 2, 4, 5, 6, 7],
            [1, 2, 4, 5, 6, 7, 0]
            """

            piv = (low + high) // 2

            if nums[piv] == target:
                return piv
            elif nums[piv] < target:
                if nums[piv] > nums[high]:
                    low = piv + 1
                else:
                    if nums[high] < target:
                        low = piv + 1
                    else:
                        high = piv - 1
            else:
                if nums[piv] < nums[high]:
                    high = piv - 1
                else:
                    if nums[low] < target:
                        high = piv - 1
                    else:
                        low = piv + 1

    return -1


if __name__ == '__main__':
    print(search([4, 5, 6, 7, 0, 1, 2], 0)) # 4
    print(search([4, 5, 6, 7, 0, 1, 2], 3)) # -1
    print(search([4, 5, 6, 7, 0, 1, 2], 5)) # 1
    print(search([5, 1, 2, 3, 4], 1)) # 1
    print(search([3, 1], 1)) # 1
