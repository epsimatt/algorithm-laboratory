# 동적 계획법

동적 계획법 (dynamic programming)은 완전 검색 알고리즘의 정확도와 욕심쟁이 알고리즘의 효율성을 합친 문제 해결 방법인데,
이 기법은 주로 하나의 문제가 여러 개의 작고 독립적인 문제로 나누어질 수 있을 때 사용할 수 있다. 동적 계획법은 가장 크거나
가장 작은 최적의 문제 해결 방법을 구하거나, 문제를 해결할 수 있는 가능한 모든 경우의 수를 구할 때 사용한다. 실력 있는
프로그래머가 되기 위해서는 동적 계획법을 제대로 이해하는 것이 매우 중요하다. 동적 계획법의 기본 개념은 비교적 간단한 반면,
동적 계획법을 실제로 문제를 해결할 때 적절히 사용하는 것은 상당히 어려운 일이기 때문이다.

## 동전 문제

6장에서 미리 보았던 동전 문제 ('다양한 종류의 동전을 개수 제한 없이 사용하여 선택한 동전의 합이 `n`이 되도록 하기 위해 
필요한 최소한의 동전 개수를 구하는 문제')를 동적 계획법을 사용해서 풀어보도록 하자. 6장에서는 가장 액수가 큰 동전부터 
차례대로 고르는 욕심쟁이 알고리즘을 사용해 문제를 해결했지만, 특별한 경우가 아니면 알고리즘을 적용해도 최적의 문제 해결 
방법을 찾을 수 없다는 단점이 있다는 것을 직접 확인해보았다.

이제 동적 계획법을 사용하여 이 문제를 해결해보도록 하자. 동적 계획법 알고리즘은 'brute force' 알고리즘처럼 동전의 합이 
될 수 있는 모든 가능성을 찾아내는 재귀 호출 함수 (recursive function)를 기반으로 하는데, 이 과정에서 메모이제이션
(memoization)이라는 기법을 사용해 효율적으로 문제를 해결한다. 메모이제이션은 동일한 계산을 반복하는 함수의 반환값을 
메모리에 저장하여 프로그램의 실행 속도를 빠르게 하는 기법이다. 동적 계획법의 핵심은 문제를 재귀 호출 함수로 이루어진
공식으로 나타내어, 여러 개의 작은 문제의 해답을 통해 하나의 큰 문제의 해답을 계산하도록 하는 것이다.

선택한 동전의 합이 `x`가 되도록 하기 위해 필요한 최소한의 동전 개수를 구하는 함수를 `solve(x)`라고 하자. 주어진 동전이 
`{1, 3, 4}`일 경우에 `solve(0) = 0, solve(1) = 1, solve(2) = 2, ..., solve(9) = 3, solve(10) = 3`이 된다. 이 함수의 
핵심은 함수가 재귀 호출을 사용하여 문제를 해결한다는 것이다. `solve(10)`에서 첫 번째 동전으로 1을 선택한다고 하면, 합이
`10 - 1 = 9`가 되는 최소한의 동전 개수를 구하면 된다. 이 방법은 첫 번째 동전으로 3이나 4를 선택했을 경우에도 똑같이
적용할 수 있다.

...

```python
from typing import List
import math


coins = [1, 3, 4]
ready = [False] * 100
value = [math.inf] * 100


def solve_v1(x: int) -> float:
    """
    주어진 동전의 집합이 `coins`일 때, 선택한 동전의 합이 `x`가 되도록 하기 위해
    필요한 최소한의 동전 개수를 구한다.
    """

    if x < 0:
        return math.inf
    elif x == 0:
        return 0
    else:
        best = math.inf

        for coin in coins:
            solution = 1 + solve_v1(x - coin)

            if best > solution:
                best = solution

        return best


def solve_v2(x: int) -> float:
    """
    주어진 동전의 집합이 `coins`일 때, 선택한 동전의 합이 `x`가 되도록 하기 위해
    필요한 최소한의 동전 개수를 구한다.
    """

    if x < 0:
        return math.inf
    elif x == 0:
        return 0
    else:
        if ready[x]:
            return value[x]
        else:
            best = math.inf

            for coin in coins:
                solution = 1 + solve_v1(x - coin)

                if best > solution:
                    best = solution

            value[x] = best
            ready[x] = True

            return best


if __name__ == '__main__':
    assert solve_v1(6) == 2 and solve_v2(6) == 2
```