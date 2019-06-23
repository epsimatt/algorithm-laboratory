from typing import List


# runtime: 13.90%, memory usage: 31.78%
def spiralOrder_v1(matrix: List[List[int]]) -> List[int]:
    result = []

    if len(matrix) == 0:
        return result

    y, x = 0, 0
    next_y, next_x = len(matrix) - 1, len(matrix[0]) - 1
    N = (next_y + 1) * (next_x + 1)

    total = 0

    result.append(matrix[0][0])

    while len(result) < N:
        # 0: right, 1: down: 2: left, 3: up
        direction = total % 4

        if direction & 1:
            for i in range(next_y):
                y += 2 - direction

                result.append(matrix[y][x])
        else:
            for j in range(next_x):
                x += 1 - direction

                result.append(matrix[y][x])

        if total > 0 and 1 - total & 1:
            next_y -= 1
            next_x -= 1

        total += 1

    return result


if __name__ == '__main__':
    print(spiralOrder_v1([]))  # []
    print(spiralOrder_v1([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(spiralOrder_v1([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])) # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
