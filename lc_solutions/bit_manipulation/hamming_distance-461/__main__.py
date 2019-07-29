# runtime: 98.03%, memory usage: 5.41%
def hammingDistance(x: int, y: int) -> int:
    target, result = x ^ y, 0

    while target > 0:
        result += target & 0b1
        target >>= 1

    return result

if __name__ == '__main__':
    result = hammingDistance(1, 4)

    print(result)