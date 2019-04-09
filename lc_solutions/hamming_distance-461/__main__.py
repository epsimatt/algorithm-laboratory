# runtime: 99.97%, memory usage: 66.23%
def hammingDistance(x: 'int', y: 'int') -> 'int':
    diff = x ^ y
    result = 0

    while diff != 0:
        if diff % 2 != 0:
            result += 1

        diff >>= 1

    return result

if __name__ == '__main__':
    result = hammingDistance(1, 4)

    print(result)