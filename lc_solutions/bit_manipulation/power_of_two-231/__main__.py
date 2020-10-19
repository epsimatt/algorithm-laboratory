# runtime: 99.95%, memory usage: 0%
def isPowerOfTwo(n: int) -> bool:
    if n < 1:
        return False

    while n > 1:
        if n % 2 != 0:
            return False

        n >>= 1

    return True


if __name__ == '__main__':
    result = isPowerOfTwo(218)

    print(result)