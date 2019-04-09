from typing import List


# runtime: 85.26%, memory usage: 32.12%
def isMonotonic(A: 'List[int]') -> 'bool':
    # increasing = 1, decreasing = 0
    state = -1

    for i in range(0, len(A) - 1):
        next = A[i + 1]
        if A[i] < next:
            if state == 0:
                return False
            else:
                state = 1
        elif A[i] > next:
            if state == 1:
                return False
            else:
                state = 0
        else:
            continue

    return True


if __name__ == '__main__':
    result = isMonotonic([1, 2, 2, 3])

    print(result)