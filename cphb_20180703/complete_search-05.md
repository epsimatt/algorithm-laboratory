# 완전 검색

완전 검색 (complete search)은 거의 모든 알고리즘 문제를 해결하는 데에 사용될 수 있는
문제 해결 방법이다. 완전 검색에서는 문제를 해결할 수 있는 모든 방법의 수를 직접 찾은
다음 (brute force), 가장 좋은 해결 방법을 선택한다. 완전 검색 기법은 주로 문제 해결에
충분한 시간이 주어질 경우에 많이 사용한다. 문제 해결에 충분한 시간이 주어지지 않을 경우에는
욕심쟁이 알고리즘 (greedy algorithm)이나 동적 계획법 (dynamic programming) 등의 기법을
사용하는 것이 좋다.

## 역추적 알고리즘
역추적 (backtracking) 알고리즘은 문제의 조건을 만족하는 모든 경우의 수를 따지며
한 단계씩 문제를 해결하는 기법이다.

## 중간 일치
중간 일치 (meet in the middle)는 분할 정복과 비슷하게 입력값을 크기가 비슷한
두 부분으로 나눈 다음, 각 부분을 따로따로 검색하여 마지막에 두 부분을 하나로
합치는 기법이다. 두 부분을 효율적으로 합칠 수 있는 방법이 존재할 경우 이 기법을
사용하면 입력값 전체를 검색할 때보다 더 짧은 실행 시간을 얻을 수 있다.

```python
from typing import List


# 집합 `s`의 모든 부분집합을 찾는다.
def subsets(s: List[int]) -> List[List[int]]:
    result = []

    # 집합 `s`의 각 원소는 비트 1개와 대응한다.
    for i in range(0, 1 << len(s)):
        subset = []

        for j in range(0, i):
            if i & (1 << j):
                subset.append(s[j])

        result.append(subset)

    return result
```