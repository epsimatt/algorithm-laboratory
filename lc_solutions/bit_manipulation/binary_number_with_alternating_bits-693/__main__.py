# runtime: 93.75%, memory usage: 5.80%
def hasAlternatingBits(n: int) -> bool:
    prev = -1

    while n > 0:
        if prev == n & 0b1:
            return False

        prev = n & 0b1
        n >>= 1

    return True


if __name__ == '__main__':
    print(hasAlternatingBits(0b101)) # True
    print(hasAlternatingBits(0b111)) # False
