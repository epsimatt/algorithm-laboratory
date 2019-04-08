from typing import List

import timeit

# 시간 복잡도: O(n^3)
def maximum_subarray_sum_v1(arr: List[int]) -> int:
    """
    Calculates the the largest possible sum of a sequence of consecutive values in the array.
    (An empty subarray is allowed)
    """
    n = len(arr)
    result = 0

    # 부분배열의 first index
    for i in range(0, n):
        # 부분배열의 last index
        for j in range(i, n):
            sum = 0

            # 부분배열 선택
            for k in range(i, j + 1):
                # 부분배열의 합 계산
                sum += arr[k]

            # 결과값 업데이트
            if result < sum:
                result = sum

    return result


# 시간 복잡도: O(n^2)
def maximum_subarray_sum_v2(arr: List[int]) -> int:
    """
    Calculates the the largest possible sum of a sequence of consecutive values in the array.
    (An empty subarray is allowed)
    """
    n = len(arr)
    result = 0

    for i in range(0, n):
        sum = 0

        for j in range(i, n):
            sum += arr[j]

            if result < sum:
                result = sum

    return result


# 시간 복잡도: O(n)
def maximum_subarray_sum_v3(arr: List[int]) -> int:
    """
    Calculates the the largest possible sum of a sequence of consecutive values in the array.
    (An empty subarray is allowed)
    """
    n = len(arr)
    result = 0
    sum = 0

    for i in range(0, n):
        if arr[i] > sum + arr[i]:
            sum = arr[i]
        else:
            sum += arr[i]

        if result < sum:
            result = sum

    return result


if __name__ == '__main__':
    result_v1 = timeit.timeit('maximum_subarray_sum_v1([-2, 1, -3, 4, -1, 2, 1, -5, 4])',
                              setup="from __main__ import maximum_subarray_sum_v1", number=10000)
    result_v2 = timeit.timeit('maximum_subarray_sum_v2([-2, 1, -3, 4, -1, 2, 1, -5, 4])',
                              setup="from __main__ import maximum_subarray_sum_v2", number=10000)
    result_v3 = timeit.timeit('maximum_subarray_sum_v3([-2, 1, -3, 4, -1, 2, 1, -5, 4])',
                              setup="from __main__ import maximum_subarray_sum_v3", number=10000)

    # 0.685468242, 0.16971708500000005, 0.064269189
    print(result_v1)
    print(result_v2)
    print(result_v3)