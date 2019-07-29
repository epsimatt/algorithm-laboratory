# runtime: 94.96%, memory usage: 48.46%
def hammingWeight(n: int) -> int:
    result = 0

    while n > 0:
        result += n & 0b1
        n >>= 1

    return result


if __name__ == '__main__':
    print(hammingWeight(0b1011)) # 3
