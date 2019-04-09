from typing import List


# runtime: 23.70%, memory usage: 0%
def subsets(nums: List[int]) -> List[List[int]]:
    subset_count = 1 << len(nums)
    result = []

    # e.g. 0b000 - 0b111
    for i in range(0, subset_count):
        tmp = []

        for j in range(0, len(nums)):
            # 특정 비트의 값이 1이라면?
            if (i >> j) & 1:
                # 비트에 대응하는 수를 임시 배열에 추가
                tmp.append(nums[j])

        result.append(tmp)

    return result


if __name__ == '__main__':
    result = subsets([1, 2, 3])

    print(result)