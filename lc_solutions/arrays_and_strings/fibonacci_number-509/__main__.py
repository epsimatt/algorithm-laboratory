# runtime: 25.85%, memory usage: 43.47%
def fib_v1(N: int) -> int:
    if N < 2:
        return N
    else:
        return fib_v1(N - 1) + fib_v1(N - 2)


seq = [0, 1] + [-1] * 29


# runtime: 92.48%, memory usage: 77.08%
def fib_v2(N: int) -> int:
    if seq[N] == -1:
        for i in range(2, N + 1):
            seq[i] = seq[i - 1] + seq[i - 2]

    return seq[N]


if __name__ == '__main__':
    print(fib_v2(2)) # 1
    print(fib_v2(3)) # 2
    print(fib_v2(4)) # 3