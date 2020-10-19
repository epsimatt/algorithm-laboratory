from typing import List


# runtime: 97.72%, memory usage: 0%
def islandPerimeter(grid: List[List[int]]) -> int:
    mx = len(grid[0]) - 1
    my = len(grid) - 1

    result = 0

    for (y, row) in enumerate(grid):
        for (x, value) in enumerate(row):
            # print("(x, y, value): ({}, {}, {})".format(x, y, value))
            if value == 1:
                if y == 0 or grid[y - 1][x] == 0:
                    result += 1

                if y == my or grid[y + 1][x] == 0:
                    result += 1

                if x == 0 or grid[y][x - 1] == 0:
                    result += 1

                if x == mx or grid[y][x + 1] == 0:
                    result += 1

    return result

if __name__ == '__main__':
    result = islandPerimeter([[0, 1, 0, 0],
                     [1, 1, 1, 0],
                     [0, 1, 0, 0],
                     [1, 1, 0, 0]])

    print(result)