# runtime: 85.28%, memory usage: 43.17%
def toHex(num: int) -> str:
    result = ""

    for _ in range(8):
        digit = num & 0b1111
        result = "0123456789abcdef"[digit] + result
        num >>= 4

        if num == 0:
            break

    return result


if __name__ == '__main__':
    result = toHex(26)
    print(result) # "1a"