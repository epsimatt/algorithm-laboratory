from typing import List


# runtime: 93.26%, memory usage: 5.33%
def generate_v1(numRows: int) -> List[List[int]]:
    result = [[1], [1, 1], [1, 2, 1]]

    if numRows < 4:
        return result[:numRows]

    for i in range(3, numRows):
        sub_res = [1] * (i + 1)

        for j in range(1, i):
            sub_res[j] = result[i - 1][j - 1] + result[i - 1][j]

        result.append(sub_res)

    return result


# runtime: 93.26%, memory usage: 57.95%
def generate_v2(numRows: int) -> List[List[int]]:
    result = []

    for i in range(0, numRows):
        sub_res = [1] * (i + 1)

        if i > 1:
            for j in range(1, i):
                sub_res[j] = result[i - 1][j - 1] + result[i - 1][j]

        result.append(sub_res)

    return result


if __name__ == '__main__':
    print(generate_v2(0))
    print(generate_v2(1))
    print(generate_v2(5))