from typing import List


# runtime: 86.94%, memory usage: 15.80%
def generateMatrix(n: int) -> List[List[int]]:
    if n == 1:
        return [[1]]
    else:
        result = [x[:] for x in [[0] * n] * n]

        border_y1 = border_x1 = 0
        border_y2, border_x2 = n - 1, n - 1
        current_number = 1

        # 오른쪽 -> 아래쪽 -> 왼쪽 -> 위쪽
        while current_number <= n * n:
            for x in range(border_x1, border_x2 + 1):
                result[border_y1][x] = current_number
                current_number += 1

            for y in range(border_y1 + 1, border_y2 + 1):
                result[y][border_x2] = current_number
                current_number += 1

            for x in range(border_x2 - 1, border_x1 - 1, -1):
                result[border_y2][x] = current_number
                current_number += 1

            for y in range(border_y2 - 1, border_y1, -1):
                result[y][border_x1] = current_number
                current_number += 1

            border_y1 += 1
            border_x1 += 1

            border_y2 -= 1
            border_x2 -= 1

        return result


if __name__ == '__main__':
    print(generateMatrix(2)) # [[1, 2], [4, 3]]
    print(generateMatrix(3)) # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    print(generateMatrix(5)) # [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]

