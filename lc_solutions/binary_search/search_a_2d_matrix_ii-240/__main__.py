from typing import List


# runtime: 67.99%, memory usage: 5.77%
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)

    if m == 0 or (m > 0 and not matrix[0]):
        return False
    else:
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] > target:
                break
            elif matrix[i][n - 1] < target:
                continue
            else:
                low, high = 0, n - 1

                while low <= high:
                    piv = int((low + high) / 2)

                    if matrix[i][piv] == target:
                        return True
                    elif matrix[i][piv] > target:
                        high = piv - 1
                    else:
                        low = piv + 1

        return False


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    print(searchMatrix(matrix, 5)) # True
    print(searchMatrix(matrix, 20)) # False