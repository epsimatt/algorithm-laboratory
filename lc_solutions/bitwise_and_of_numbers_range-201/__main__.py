# runtime: 98.27%, memory usage: 0%
def rangeBitwiseAnd(m: int, n: int) -> int:
    i = 0
    result = 0

    # 공통 비트가 나올 때까지 계속 right-shift 해준다.
    # 두 수가 공통으로 가지고 있는 비트를 모두 구하면 값이 나올 것!
    while m != n:
        m >>= 1
        n >>= 1

        i += 1

    result += m << i

    return result

if __name__ == '__main__':
    result = rangeBitwiseAnd(5, 7)

    print(result)
