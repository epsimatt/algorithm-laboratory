from typing import List


# runtime: 87.54%, memory usage: 100%
def pivotIndex(nums: List[int]) -> int:
    n = len(nums)

    if n > 0:
        left_sum, right_sum = 0, sum(nums) - nums[0]

        for i in range(1, n + 1):
            if left_sum == right_sum:
                return i - 1

            if i > 0:
                left_sum += nums[i - 1]

            if i < n:
                right_sum -= nums[i]

    return -1


if __name__ == '__main__':
    print(pivotIndex([1, 7, 3, 6, 5, 6])) # 3
    print(pivotIndex([-1, -1, -1, 0, 1, 1])) # 0
    print(pivotIndex([1, 2, 3])) # -1
