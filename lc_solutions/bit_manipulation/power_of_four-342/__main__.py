# runtime: 79.84%, memory usage: 5.81%
def isPowerOfFour(num: int) -> bool:
    # return num & (num - 1) == (num - 1) % 3 == 0
    zero_count = 0

    if num <= 0:
        return False

    while num > 1:
        if num & 1:
            return False
        else:
            zero_count += 1

        num >>= 1

    return zero_count & 1 == 0


if __name__ == '__main__':
    print(isPowerOfFour(2)) # False
    print(isPowerOfFour(4)) # True
    print(isPowerOfFour(-64)) # False
