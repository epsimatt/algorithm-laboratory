# runtime: 64.94%, memory usage: 0%
def reverseBits(n):
    result = 0

    for i in range(0, 32):
        result += ((n >> i) & 1) << (31 - i)

    return result


if __name__ == '__main__':
    result = reverseBits(0b00000010100101000001111010011100)

    print(result)