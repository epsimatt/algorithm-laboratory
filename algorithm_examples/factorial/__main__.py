import timeit

# `n!`의 값을 계산한다.
def factorial(n: int) -> int:
    if n != 0:
        return n * factorial(n - 1)
    else:
        return 1

if __name__ == '__main__':
    result = timeit.timeit('factorial(20)', setup="from __main__ import factorial", number=10000)

    # 0.088428293
    print(result)