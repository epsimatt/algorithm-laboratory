# runtime: 64.94%, memory usage: 81.57%
def reverseBits_v1(n):
    result = 0

    for i in range(0, 32):
        result += ((n >> i) & 1) << (31 - i)

    return result


# runtime: 92.13%, memory usage: 57.97%
def reverseBits_v2(n):
    result = 0

    for i in range(0, 32):
        rev_bit = (n >> i) & 1

        if rev_bit > 0:
            result += rev_bit << (31 - i)

    return result


if __name__ == '__main__':
    result = reverseBits_v2(0b00000010100101000001111010011100)

    print(bin(result))