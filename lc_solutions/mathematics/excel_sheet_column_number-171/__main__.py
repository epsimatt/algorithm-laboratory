# runtime: 65.01%, memory usage: 0%
def titleToNumber(s: str) -> int:
    """
    A = 26^0 * 1, Z = 26^0 * 26
    AA = 26^1 + 26^0 * 1, ZZ = 26^1 * 26 + 26^0 * 1
    AAA = 26^2 + 26^1 * 1 + 26^0 * 1, AAZ = 26^2 * 1 + 26^1 * 1 + 26^0 * 26
    AAAA = 26^3 * 1 + 26^2 * 1 + 26^1 * 1, 26^0 * 1
    """

    """
    result = 0

    for i in range(0, len(s)):
        j = len(s) - i - 1

        result += (26 ** j) * (ord(s[i]) - 64)

    return result
    """

    result = 0

    for i, c in enumerate(s[::-1]):
        result += (26 ** i) * (ord(c) - 64)

    return result


if __name__ == '__main__':
    result = titleToNumber("ZY")

    print(result)