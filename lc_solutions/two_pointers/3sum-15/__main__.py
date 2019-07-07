from typing import List


# runtime: 74.12%, memory usage: 55.02%
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    # `i + 1`번째 원소부터 탐색 시작
    for i in range(len(nums) - 2):
        # 0보다 커지면 탐색 종료
        if nums[i] > 0:
            break

        # 중복 원소는 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]

        low = i + 1
        high = len(nums) - 1

        while low < high:
            if nums[low] + nums[high] == target:
                result.append([nums[i], nums[low], nums[high]])

                low += 1
                high -= 1

                while low < high and nums[low] == nums[low - 1]:
                    low += 1

                while low < high and nums[high] == nums[high + 1]:
                    high -= 1
            elif nums[low] + nums[high] < target:
                low += 1
            else:
                high -= 1

    return result


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4])) # [[-1, -1, 2], [-1, 0, 1]]
    print(threeSum([-3, -2, -1, 0, 1, 2])) # [[-3, 1, 2], [-2, 0, 2], [-1, 0, 1]]
    print(threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])) # [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
