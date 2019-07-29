tribonacci_seq = [0, 1, 1]


# runtime: 100%, memory usage: 100%
def tribonacci(n: int) -> int:
    k = len(tribonacci_seq)

    if k < n + 1:
        for i in range(k - 3, n - 2):
            tribonacci_seq.append(tribonacci_seq[i] + tribonacci_seq[i + 1] + tribonacci_seq[i + 2])

    return tribonacci_seq[n]


if __name__ == '__main__':
    print(tribonacci(4)) # 4
    print(tribonacci(25)) # 1389597