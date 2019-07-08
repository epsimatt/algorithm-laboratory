from typing import List


# time limit exceeded
def threeSum_v1(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    # `i + 1`번째 원소부터 탐색 시작
    for i in range(len(nums) - 2):
        target = -nums[i]

        low = i + 1
        high = len(nums) - 1

        while low < high:
            if nums[low] + nums[high] == target:
                sub_result = [nums[i], nums[low], nums[high]]

                if sub_result not in result:
                    result.append(sub_result)

                low += 1
                high -= 1
            elif nums[low] + nums[high] < target:
                low += 1
            else:
                high -= 1

    return result


# time limit exceeded
def threeSum_v2(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # 0보다 커지면 탐색 종료
        if nums[i] > 0:
            break

        target = -nums[i]

        low = i + 1
        high = len(nums) - 1

        while low < high:
            if nums[low] + nums[high] == target:
                sub_result = [nums[i], nums[low], nums[high]]

                if sub_result not in result:
                    result.append(sub_result)

                low += 1
                high -= 1
            elif nums[low] + nums[high] < target:
                low += 1
            else:
                high -= 1

    return result


# time limit exceeded
def threeSum_v3(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
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
                sub_result = [nums[i], nums[low], nums[high]]

                if sub_result not in result:
                    result.append(sub_result)

                low += 1
                high -= 1
            elif nums[low] + nums[high] < target:
                low += 1
            else:
                high -= 1

    return result


# runtime: 74.12%, memory usage: 55.06%
def threeSum_v4(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break

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

                # 왼쪽부터 중복 원소 건너뛰기
                while low < high and nums[low] == nums[low - 1]:
                    low += 1

                # 오른쪽부터 중복 원소 건너뛰기
                while low < high and nums[high] == nums[high + 1]:
                    high -= 1
            elif nums[low] + nums[high] < target:
                low += 1
            else:
                high -= 1

    return result


if __name__ == '__main__':
    print(threeSum_v4([-1, 0, 1, 2, -1, -4])) # [[-1, -1, 2], [-1, 0, 1]]
    print(threeSum_v4([-3, -2, -1, 0, 1, 2])) # [[-3, 1, 2], [-2, 0, 2], [-1, 0, 1]]
    print(threeSum_v4([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])) # [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
