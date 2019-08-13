from typing import List

import math
import timeit


def sieve_of_eratosthenes_v1(n: int) -> List[int]:
    result = [x for x in range(0, n + 1)]

    for i in range(2, n + 1):
        # 선택한 수가 아직 지워지지 않은 수라면?
        if result[i] != 0:
            for j in range(1, int(n / i)):
                # i의 배수에 대응하는 index
                k = i * (j + 1)

                # 선택한 수를 지운다.
                result[k] = 0

    # 0과 1은 소수가 아니기 때문에 모두 지운다.
    return [x for x in result if x > 1]


def sieve_of_eratosthenes_v2(n: int) -> List[int]:
    result = [x for x in range(0, n + 1)]

    # https://en.wikipedia.org/wiki/Prime_number#Trial_division
    for i in range(2, int(math.sqrt(n))):
        if result[i] != 0:
            for j in range(1, int(n / i)):
                k = i * (j + 1)

                result[k] = 0

    return [x for x in result if x > 1]


def sieve_of_eratosthenes_v3(n: int) -> List[int]:
    i, result = 2, [x for x in range(0, n + 1)]

    while i * i <= n:
        if result[i] != 0:
            for j in range(1, int(n / i)):
                k = i * (j + 1)

                result[k] = 0

        i += 1

    return [x for x in result if x > 1]


if __name__ == '__main__':
    result_v1 = timeit.timeit('sieve_of_eratosthenes_v1(10000)',
                              setup="from __main__ import sieve_of_eratosthenes_v1", number=100)
    result_v2 = timeit.timeit('sieve_of_eratosthenes_v2(10000)',
                              setup="from __main__ import sieve_of_eratosthenes_v2", number=100)
    result_v3 = timeit.timeit('sieve_of_eratosthenes_v3(10000)',
                              setup="from __main__ import sieve_of_eratosthenes_v3", number=100)

    print(result_v1) # 0.7293963
    print(result_v2) # 0.4852364
    print(result_v3) # 0.4208772
