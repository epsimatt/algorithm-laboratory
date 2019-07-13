from typing import List


# runtime: 11.46%, memory usage: 30.00%
def threeSumClosest_v1(nums: List[int], target: int) -> int:
    nums.sort()

    n = len(nums)

    result = float('inf')

    for i in range(n - 2):
        low, high = i + 1, n - 1

        while low < high:
            three_sum = nums[i] + nums[low] + nums[high]

            diff_ts = three_sum - target
            diff_rs = result - target

            if abs(diff_rs) > abs(diff_ts):
                result = three_sum

            if diff_ts > 0:
                high -= 1
            else:
                low += 1

    return result


# runtime: %, memory usage: %
def threeSumClosest_v2(nums: List[int], target: int) -> int:
    pass


if __name__ == '__main__':
    print(threeSumClosest_v2([-1, 2, 1, -4], 1)) # -1 + 2 + 1 = 2
    print(threeSumClosest_v2([0, 2, 1, -3], 1)) # 2 + 1 - 3 = 0
    print(threeSumClosest_v2([1, 1, -1, -1, 3], -1)) # 1 - 1 - 1 = -1
