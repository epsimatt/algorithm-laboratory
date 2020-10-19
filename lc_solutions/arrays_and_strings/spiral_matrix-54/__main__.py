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


# runtime: 91.05%, memory usage: 82.26%
def spiralOrder_v2(matrix: List[List[int]]) -> List[int]:
    if len(matrix) == 0:
        return []
    elif len(matrix) == 1:
        return matrix[0]
    else:
        result = []

        begin_y, begin_x = 0, 0
        end_y, end_x = len(matrix), len(matrix[0])

        N = end_y * end_x

        while len(result) < N:
            if begin_x == end_x:
                result.append(matrix[begin_x][begin_y])
            else:
                for current_x in range(begin_x, end_x):
                    end_x = current_x
                    result.append(matrix[begin_y][current_x])

                if len(result) == N:
                    break

                for current_y in range(begin_y + 1, end_y):
                    end_y = current_y
                    result.append(matrix[current_y][end_x])

                if begin_y < end_y and begin_x < end_x:
                    for current_x in range(end_x - 1, begin_x - 1, -1):
                        begin_x = current_x
                        result.append(matrix[end_y][current_x])

                    for current_y in range(end_y - 1, begin_y, -1):
                        begin_y = current_y
                        result.append(matrix[current_y][begin_x])

                    begin_x += 1

        return result


if __name__ == '__main__':
    print(spiralOrder_v2([]))  # []
    print(spiralOrder_v2([[2, 3]]))  # []
    print(spiralOrder_v2([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(spiralOrder_v2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])) # [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    print(spiralOrder_v2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])) # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
