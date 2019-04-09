from typing import List


# runtime: 99.69%, memory usage: 91.85%
def sortedSquares(A: 'List[int]') -> 'List[int]':
    result = [n * n for n in A]
    result.sort()

    return result


if __name__ == '__main__':
    result = sortedSquares([-4, -1, 0, 3, 10])

    print(result)