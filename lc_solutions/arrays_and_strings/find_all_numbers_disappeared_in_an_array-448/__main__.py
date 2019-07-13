from typing import List


# runtime: 73.69%, memory usage: 27.81%
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    n = len(nums)

    if n == 0:
        return []
    else:
        nums = list(set(nums))

        checked = [False] * n
        result = []

        for i in range(len(nums)):
            checked[nums[i] - 1] = True

        for i in range(n):
            if not checked[i]:
                result.append(i + 1)

        return result


if __name__ == '__main__':
    print(findDisappearedNumbers([1, 1])) # [2]
    print(findDisappearedNumbers([2, 2])) # [1]
    print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])) # [5, 6]
