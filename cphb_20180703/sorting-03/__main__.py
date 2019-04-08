"""
정렬 (sorting)은 기본적인 알고리즘 디자인 문제 중 하나이다. 배열의 원소가 정렬되어 있으면 데이터를 더 빠르게 처리할 수
있기 때문에, 대다수의 효율적인 알고리즘은 정렬을 사용한다. 일반적으로, 효율적인 정렬 알고리즘의 시간 복잡도는
O(n * log n)이라고 알려져 있다.

버블 정렬 (bubble sort)처럼 구현이 간단한 알고리즘의 시간 복잡도는 O(n^2) 정도이다. 이러한 알고리즘은 보통 두 개의 중첩된
반복문이 있고 코드가 비교적 단순하고 짧은 것이 특징이다.
"""

from typing import List

import timeit

# 배열의 인접한 두 원소의 순서를 바꾸어, 큰 원소일수록 오른쪽으로 가게 하는 버블 정렬을 실행한다.
# 시간 복잡도: O(n^2)
def bubble_sort(arr: List[int]):
    """
    fn bubble_sort(v: &mut Vec<usize>) {
        for i in 1..(v.len()) {
            for j in 0..(v.len() - i) {
                if v[j] > v[j + 1] {
                    // https://doc.rust-lang.org/std/primitive.slice.html#method.swap
                    let t = v[j + 1];
                    v[j + 1] = v[j];
                    v[j] = t;
                }
            }
        }
    }
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


# 정해진 배열에서 최솟값을 선택해 맨 왼쪽으로 옮기는 선택 정렬을 실행한다.
def selection_sort(arr: List[int]):
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

    # 0.27574128, 0.20391832799999998
    print(result_bubble, result_selection)