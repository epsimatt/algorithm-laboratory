# runtime: 100.00%, memory usage: 13.89%
def findComplement(num: 'int') -> 'int':
    """
    101 ^ 111 = 010
    11010 ^ 11111 = 00101

    1 = 1
    11 = 2 + 1
    111 = 4 + 2 + 1
    1111 = 8 + 4 + 2 + 1
    11111 = 16 + 8 + 4 + 2 + 1
    ...
    """

    r = 1

    while r <= num:
        # r *= 2
        r <<= 1

    return num ^ (r - 1)

if __name__ == '__main__':
    result = findComplement(5)

    print(result)