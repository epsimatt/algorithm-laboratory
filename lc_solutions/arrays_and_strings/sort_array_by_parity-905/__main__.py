from typing import List


# runtime: 99.84%, memory usage: 28.25%
def sortArrayByParity(A: 'List[int]') -> 'List[int]':
    evens = []
    odds = []

    for n in A:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)

    return evens + odds

if __name__ == '__main__':
    result = sortArrayByParity([3, 1, 2, 4])

    print(result)