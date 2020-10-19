from typing import List


# runtime: 81.98%, memory usage: 5.11%
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)

    if n == 0 or (n > 0 and not matrix[0]):
        return False
    else:
        for i in range(n):
            if matrix[i][0] > target:
                break
            elif len(matrix[i]) == 1:
                if target in matrix[i]:
                    return True
            else:
                low = 0
                high = len(matrix[0]) - 1

                while low <= high:
                    piv = int((low + high) / 2)
                    val = matrix[i][piv]

                    if val == target:
                        return True
                    elif val > target:
                        high = piv - 1
                    else:
                        low = piv + 1

        return False


if __name__ == '__main__':
    print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)) # True
    print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13)) # False
    print(searchMatrix([[1], [3]], 1)) # True
    print(searchMatrix([[1, 3]], 3))  # True
    print(searchMatrix([[1]], 1))  # True
    print(searchMatrix([[]], 1)) # False
    print(searchMatrix([], 0)) # False
