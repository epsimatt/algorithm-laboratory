from typing import List


# runtime: 21.81%, memory usage: 52.82%
def twoSum(nums: List[int], target: int) -> List[int]:
    # 첫 번째 숫자 선택
    for i, v in enumerate(nums):
        # 두 번째 숫자 선택
        for j, w in enumerate(nums[i + 1:]):
            if v + w == target:
                return [i, i + j + 1]


if __name__ == '__main__':
    result = twoSum([2, 7, 11, 15], 9)

    print(result)