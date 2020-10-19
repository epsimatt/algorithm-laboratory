from typing import List


# time limit exceeded
def rob_v1(nums: List[int]) -> int:
    n = len(nums)

    if n == 0:
        return 0
    elif n < 3:
        return max(nums)
    else:
        result = 0

        for i in range(n - 1):
            result = max(result, nums[i] + rob_v1(nums[(i + 2):]))

        return result


# runtime: 97.96%, memory usage: 49.14%
def rob_v2(nums: List[int]) -> int:
    n = len(nums)

    """
    예시: `nums = [2, 7, 9, 3, 1]`일 때,

    `nums[0]`는 배열 `[2]`의 최댓값, 따라서 2가 된다.
    `nums[1]`은 배열 `[2, 7]`의 최댓값, 따라서 7이 된다.
    `nums[2]`는 배열 `[2, 7, 9]`에서 9 + (배열 `[2]`에서 털 수 있는 금액의 최댓값)과 7 중 더 큰 값, 따라서 11이 된다.
    `nums[3]`은 배열 `[2, 7, 9, 3]`에서 3 + (배열 `[2, 7]`에서 털 수 있는 금액의 최댓값)과 9 + (배열 `[2]`에서 털 수 있는 
    금액의 최댓값) 중 더 큰 값, 따라서 11이 된다.

    ...
    """

    if n == 0:
        return 0
    elif n < 3:
        return max(nums)
    else:
        table = [nums[0], max(nums[:2])] + [-1] * (n - 2)

        for i in range(2, n):
            table[i] = max(table[i - 2] + nums[i], table[i - 1])

        return table[n - 1]


if __name__ == '__main__':
    print(rob_v2([1, 3, 1]))  # 3
    print(rob_v2([1, 1, 1, 2]))  # 1 + 2 = 3
    print(rob_v2([1, 2, 3, 1]))  # 1 + 3 = 4
    print(rob_v2([2, 7, 9, 3, 1]))  # 2 + 9 + 1 = 12
