from typing import List


# runtime: 76.53%, memory usage: 5.33%
def transpose(A: List[List[int]]) -> List[List[int]]:
    my, mx = len(A), len(A[0])
    result = [m[:] for m in [[]] * mx]

    for x in range(mx):
        for y in range(my):
            result[x].append(A[y][x])

    return result


if __name__ == '__main__':
    print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
