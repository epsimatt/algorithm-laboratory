from typing import List


# runtime: 99.62%, memory usage: 62.69%
def maxSubArray(nums: List[int]) -> int:
    best = nums[0]
    sum = 0

    for i in range(0, len(nums)):
        if nums[i] < sum + nums[i]:
            sum += nums[i]
        else:
            sum = nums[i]

        if best < sum:
            best = sum

    return best


if __name__ == '__main__':
    result = maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])

    print(result)