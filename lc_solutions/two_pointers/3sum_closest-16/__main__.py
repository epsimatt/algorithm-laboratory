from typing import List


# runtime: 21.83%, memory usage: 54.23%
def threeSumClosest_v1(nums: List[int], target: int) -> int:
    nums.sort()

    n = len(nums)

    result = float('inf')

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        low, high = i + 1, n - 1

        while low < high:
            three_sum = nums[i] + nums[low] + nums[high]

            diff_ts = three_sum - target
            diff_rs = result - target

            if abs(diff_rs) > abs(diff_ts):
                result = three_sum

            if three_sum == target:
                return three_sum
            elif three_sum < target:
                low += 1
            else:
                high -= 1

    return result


# runtime: 88.58%, memory usage: 23.07%
def threeSumClosest_v2(nums: List[int], target: int) -> int:
    nums.sort()

    result = float('inf')

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        low, high = i + 1, len(nums) - 1

        while low < high:
            three_sum = nums[i] + nums[low] + nums[high]

            diff_ts = three_sum - target
            diff_rs = result - target

            if abs(diff_rs) > abs(diff_ts):
                result = three_sum

            if three_sum == target:
                return three_sum
            elif three_sum < target:
                while low < high and nums[low] == nums[low + 1]:
                    low += 1
                low += 1
            else:
                while low < high and nums[high] == nums[high - 1]:
                    high -= 1
                high -= 1

    return result


if __name__ == '__main__':
    print(threeSumClosest_v2([-1, 2, 1, -4], 1)) # -1 + 2 + 1 = 2
    print(threeSumClosest_v2([0, 2, 1, -3], 1)) # 2 + 1 - 3 = 0
    print(threeSumClosest_v2([1, 1, -1, -1, 3], -1)) # 1 - 1 - 1 = -1
