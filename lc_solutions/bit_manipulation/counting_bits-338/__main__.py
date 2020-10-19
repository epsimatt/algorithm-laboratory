from typing import List


# runtime: 5.16%, memory usage: 0%
def countBits(num: int) -> List[int]:
    result = list()

    for i in range(0, num + 1):
        tmp = i
        j = 0

        while tmp != 0:
            if tmp & 1 == 1:
                j += 1

            tmp >>= 1

        result.append(j)

    return result


if __name__ == '__main__':
    result = countBits(5)

    print(result)