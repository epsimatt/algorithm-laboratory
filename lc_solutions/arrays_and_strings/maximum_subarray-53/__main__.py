from typing import List


# time limit exceeded
def maxSubArray_v1(nums: List[int]) -> int:
    n = len(nums)

    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    else:
        res = -float('inf')

        for i in range(0, n):
            for j in range(i, n):
                sub_res = sum(nums[i:j + 1])

                if res < sub_res:
                    res = sub_res

        return res


# runtime: 99.61%, memory usage: 84.99%
def maxSubArray_v2(nums: List[int]) -> int:
    n = len(nums)

    result, sub_res = -float('inf'), 0

    for i in range(0, n):
        if sub_res + nums[i] > nums[i]:
            sub_res += nums[i]
        else:
            sub_res = nums[i]

        if result < sub_res:
            result = sub_res

    return result


if __name__ == '__main__':
    print(maxSubArray_v2([-1])) # -1
    print(maxSubArray_v2([1])) # 1
    print(maxSubArray_v2([-2, 1]))  # 1
    print(maxSubArray_v2([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6 ([4, -1, 2, 1])