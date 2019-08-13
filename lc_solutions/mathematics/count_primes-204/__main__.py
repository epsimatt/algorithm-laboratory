# time limit exceeded
def countPrimes_v1(n: int) -> int:
    result = 0

    for i in range(2, n):
        is_prime = True

        for j in range(2, i - 1):
            if i % j == 0:
                is_prime = False

        result += int(is_prime)

    return result


# time limit exceeded
def countPrimes_v2(n: int) -> int:
    result = 0

    def is_prime(k: int) -> bool:
        i = 2

        while i * i <= k:
            if k % i == 0:
                return False

            i += 1

        return True

    for i in range(2, n):
        if is_prime(i):
            result += 1

    return result


# runtime: 26.88%, memory usage: 27.59%
def countPrimes_v3(n: int) -> int:
    i, is_prime = 2, [x for x in range(0, n)]

    while i * i <= n - 1:
        if is_prime[i] != 0:
            for j in range(1, int((n - 1) / i)):
                k = i * (j + 1)

                is_prime[k] = 0

        i += 1

    return len([x for x in is_prime if x > 1])


if __name__ == '__main__':
    print(countPrimes_v3(10)) # 4
