from typing import List

rows = [[1]] + [[0]] * 34


# runtime: 80.37%, memory usage: 60.90%
def getRow(rowIndex: int) -> List[int]:
    if not rows[rowIndex][0]:
        generated_row = [1] * (rowIndex + 1)

        for j in range(1, rowIndex):
            generated_row[j] = getRow(rowIndex - 1)[j - 1] + getRow(rowIndex - 1)[j]

        rows[rowIndex] = generated_row

    return rows[rowIndex]


if __name__ == '__main__':
    print(getRow(10))
    print(getRow(5))