# 정렬과 탐색

정렬 (sorting)은 기본적인 알고리즘 디자인 문제 중 하나이다. 배열의 원소가 정렬되어 있으면 데이터를 더 빠르게 처리할 수
있기 때문에, 대다수의 효율적인 알고리즘은 정렬을 사용한다. 일반적으로, 효율적인 정렬 알고리즘의 시간 복잡도는
O(n * log n)이라고 알려져 있다. 버블 정렬 (bubble sort)처럼 구현이 간단한 알고리즘의 시간 복잡도는 O(n^2) 정도인데, 
이러한 알고리즘은 보통 두 개의 중첩된 반복문이 있고 코드가 비교적 단순하고 짧은 것이 특징이다.

## 분할 정복

분할 정복 (divide and conquer / divide et impera)는 복잡한 문제를 작은 문제로 분해한 뒤에, 작은 문제의 해답을 모아 원래의 문제의 답을 구하는
문제 해결 방법이다. 분할 정복은 크게 세 단계로 나눌 수 있다. 첫 번째 단계는 복잡한 문제를 작은 문제로 분해하는
분해 (divide) 과정, 두 번째 단계는 작은 문제의 해답을 구하는 정복 (conquer) 과정이고, 마지막 단계는 작은 문제의 해답을
합치는 결합 (combine) 과정이다. 분할 정복 알고리즘의 예로는 이진 탐색 (binary search), 병합 정렬 (merge sort), 퀵 정렬 (quick sort),
팀 정렬 (https://hackernoon.com/timsort-the-fastest-sorting-algorithm-youve-never-heard-of-36b28417f399) 등이
있다.

## 탐색

배열에서 특정 원소를 찾는 일반적인 방법은 아래와 같이 `for` 반복문을 사용해서 배열에 들어 있는 모든 원소를 확인하는 것이다.

```c
for (int i = 0; i < n; i++) {
    if (array[i] == x) {
        // x found at index i
    }
}
```

이 코드는 최악의 경우 특정 원소를 찾기 위해 배열의 모든 원소를 확인해야 하므로 시간 복잡도는 `O(n)`이다.
배열의 정렬되지 않은 경우 이 코드는 최선의 선택이 될 수 있지만, 배열이 정렬되어 있는 경우에는 상황이 달라진다.
배열이 이미 정렬되어 있는 경우, 이진 탐색 알고리즘을 사용하면 시간 복잡도가 `O(log n)`이 되어, 실행 시간이 매우 짧아진다.

...

```python
from typing import List

import timeit


def linear_search(arr: List[int], x: int) -> int:
    """
    선형 검색 알고리즘을 사용해 배열의 모든 원소를 하나하나 확인해가며 특정 원소를 찾는다.
    (시간 복잡도: O(n))
    """
    for index, element in enumerate(arr):
        if element == x:
            return index

    return -1


def binary_search(arr: List[int], x: int) -> int:
    """
    이진 탐색 알고리즘을 사용해 정렬되어 있는 배열에서 특정한 원소를 찾는다.
    (시간 복잡도: O(log n))
    """
    left_index = 0
    right_index = len(arr) - 1

    while left_index < right_index:
        pivot_index = int((left_index + right_index) / 2)

        if arr[pivot_index] == x:
            return pivot_index

        # `pivot_index`에 있는 원소가 `x`보다 작으면?
        if arr[pivot_index] < x:
            # `pivot_index` 다음부터 검색
            left_index = pivot_index + 1
        else:
            # `pivot_index` 바로 전까지 검색
            right_index = pivot_index - 1

    return -1


def bubble_sort(arr: List[int]):
    """
    배열의 인접한 두 원소의 순서를 바꾸어, 큰 원소일수록 오른쪽으로 가게 하는 버블 정렬을 실행한다.
    (시간 복잡도: O(n^2))
    """
    n = len(arr)

    # 정렬이 끝난 원소의 index
    for i in range(1, n):
        for j in range(0, n - i):
            if arr[j] > arr[j + 1]:
                # `arr[j]`와 `arr[j + 1]`의 값을 서로 바꾼다.
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp


def merge_sort(arr: List[int], left_index: int, right_index: int):
    """
    배열을 두 부분으로 나누어 각각의 배열을 정렬한 다음, 두 배열을 하나로 합치는 병합 정렬을 실행한다.
    (시간 복잡도: O(n * log n))
    
    병합 정렬의 실행 순서는 아래와 같다.

    1. `left_index`와 `right_index`의 값이 같다면, 아무 것도 하지 않는다.
    2. 배열의 기준값의 index를 구한다.
    3. 배열을 두 개로 나누고 정렬한다.
    4. 정렬된 배열 두 개를 하나로 합친다.
    """

    # 특정 계산을 위해 알고리즘에서 임의로 선택되는 값을 기준값 또는 피벗 (pivot)이라고 한다.
    pivot_index = int((left_index + right_index) / 2)

    if left_index < right_index:
        merge_sort(arr, left_index, pivot_index)
        merge_sort(arr, pivot_index + 1, right_index)

        left_arr = arr[left_index:(pivot_index + 1)]
        right_arr = arr[(pivot_index + 1):(right_index + 1)]

        i = 0
        j = 0
        k = left_index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1

            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


def selection_sort(arr: List[int]):
    """
    정해진 배열에서 최솟값을 선택해 맨 왼쪽으로 옮기는 선택 정렬을 실행한다.
    (시간 복잡도: O(n^2))
    """
    n = len(arr)

    """
    i: 0, j: arr[1..N]
    i: 1, j: arr[2..N]
    i: 2, j: arr[3..N]

    ...
    """
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp


if __name__ == '__main__':
    result_bubble = timeit.timeit('bubble_sort([4, 8, 6, 5, 2, 1, 3, 9, 7, 10])',
                                  setup="from __main__ import bubble_sort", number=10000)

    result_selection = timeit.timeit('selection_sort([4, 8, 6, 5, 2, 1, 3, 9, 7, 10])',
                                     setup="from __main__ import selection_sort", number=10000)

    result_merge = timeit.timeit('merge_sort([4, 8, 6, 5, 2, 1, 3, 9, 7, 10], 0, 9)',
                                 setup="from __main__ import merge_sort", number=10000)

    print(result_bubble, result_selection, result_merge)
```