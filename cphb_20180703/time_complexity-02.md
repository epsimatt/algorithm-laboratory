# 시간 복잡도

알고리즘의 시간 복잡도 (time complexity)는 처리해야 될 입력값의 크기와 실행 시간의 관계를 나타내는 함수이다.
시간 복잡도는 알고리즘의 효율성을 평가하는 데에 사용되며, 시간 복잡도를 계산하여 알고리즘을 구현하기 전에
알고리즘이 어느 정도로 빠른지 알아볼 수 있다.

알고리즘의 시간 복잡도는 주로 Paul Bachmann과 Edmund Landau가 만든 Big-O Notation을 통해 나타낸다.
`O(···)`의 시간 복잡도에서 `···`는 함수를 나타내고, 일반적으로 변수 `n`은 문자열의 길이나 배열의 크기 같은
입력값의 크기를 나타낸다.

## 시간 복잡도 계산 방법

- 반복문이 k개 중첩되어 있을 때, 이 알고리즘의 시간 복잡도는 `O(n^k)`이다.
- 알고리즘이 여러 단계 (phase)로 나누어져 있을 때, 이 알고리즘의 시간 복잡도는 가장 큰 시간 복잡도를 가지는 단계의
시간 복잡도이다.
- 변수의 개수는 알고리즘의 시간 복잡도에 영향을 준다.
- 재귀 함수 (recursive function)의 시간 복잡도는 함수가 몇 번 호출되었는지, 함수가 한 번
호출되었을 때 시간 복잡도는 어떻게 되는지에 따라 달라진다.

## 시간 복잡도 예시
- `O(1)`: 입력값의 크기에 영향을 받지 않는 상수 시간 알고리즘 (constant-time algorithm)
- `O(log n)`: 입력값의 크기를 각 단계마다 줄여나가는 로그 알고리즘 (logarithmic algorithm)
- `O(√n)`: `O(log n)`보다는 느리지만 `O(n)`보다는 빠른, 제곱근 알고리즘 (square root algorithm)
- `O(n)`: 모든 경우의 수를 하나하나씩 다 따지는 선형 알고리즘 (linear algorithm)
- `O(n * log n)`: 입력값을 정렬하는 알고리즘이거나 (가장 효율적인 정렬 알고리즘의 시간 복잡도가 `O(n * log n)`이기 때문에)
연산 수행 시간이 `O(log n)`정도 걸리는 자료 구조를 사용하는 알고리즘
- `O(n^2)`, `O(n^3)`: 여러 개의 반복문이 중첩되어 있는 알고리즘 (quadratic / cubic algorithm)
- `O(2^n)`: 입력값의 모든 부분집합을 찾는 알고리즘
- `O(n!)`: 서로 다른 n개에서 중복 없이 r개를 뽑아 나열하는 순열 (permutation)

## 알고리즘의 효율성 평가하기 
(input size, required time complexity)
- (n <= 10, `O(n!)`)
- (n <= 20, `O(2^n)`)
- (n <= 500, `O(n^3)`)
- (n <= 5000, `O(n^2)`)
- (n <= 10^6, `O(n * log n)` or `O(n)`)
- (n is large, `O(1)` or `O(log n)`)

일반적으로, 알고리즘의 시간 복잡도가 최악의 경우 `O(n^k)` (단, `k`는 상수)일 때, 이 알고리즘을 다항 시간 알고리즘
(polynomial algorithm)이라고 한다. `O(2^n)`과 `O(n!)`을 제외한 위 예시의 모든 알고리즘은 다항 시간 알고리즘이다.
대부분의 경우 상수 `k`는 아주 작기 때문에, 어떤 알고리즘이 다항 시간 복잡도를 가진다는 것은 곧 알고리즘이 효율적이라는
것을 의미한다. NP-난해 (NP-hard) 문제는 다항 시간 알고리즘이 알려져 있지 않은 모든 프로그래밍 문제이다.

```python
# 시간 복잡도: O(n^2)
def phases(n: int):
    # 시간 복잡도: O(n)
    for i in range(1, n):
        pass

    # 시간 복잡도: O(n^2)
    for i in range(1, n):
        for j in range(1, n):
            pass


# 시간 복잡도: O(n * m)
def several_variables(n: int, m: int):
    for i in range(1, n):
        for j in range(1, m):
            pass


# recursion(n)을 호출하면 총 n번의 함수 호출이 발생하게 되고, 각 호출의 시간 복잡도는 O(1)이다.
# 시간 복잡도: O(n * 1)
def recursion_one(n: int):
    if n == 1:
        return

    recursion_one(n - 1)


# n = 1일 때를 제외하면 이 함수는 한 번 호출될 때마다 두 번의 함수 호출이 더 발생하게 된다.
# g(n)일 때 함수 호출은 2^0번, g(n - 1)일 때 2^1번, g(n - 2)일 때 2^2번, ···, g(1)일 때 2^(n - 1)번
# 시간 복잡도: O(1 + 2 + 4 + ··· + 2^(n - 1)) = O(2^n - 1) = O(2^n)
def recursion_two(n: int):
    if n == 1:
        return

    recursion_two(n - 1)
    recursion_two(n - 1)
```

> 참고: Big-O Algorithm Complexity Cheat Sheet
>
> http://bigocheatsheet.com/