# runtime: 67.50%, memory usage: 6.67%
def bitwiseComplement(N: int) -> int:
    if N < 2:
        return 1 - (N & 1)
    else:
        result, i = 0, 0

        while N > 1:
            result += (1 - (N & 1)) << i

            N >>= 1
            i += 1

        return result


if __name__ == '__main__':
    print(bitwiseComplement(5)) # 2
    print(bitwiseComplement(7)) # 0
    print(bitwiseComplement(10)) # 5
