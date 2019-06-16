def isPerfectSquare(num: int) -> bool:
    low = 1
    high = num

    while low <= high:
        pivot = int((low + high) / 2)

        if pivot * pivot < num:
            low = pivot + 1
        elif pivot * pivot > num:
            high = pivot - 1
        else:
            return True

    return False


if __name__ == '__main__':
    print(isPerfectSquare(1))
    print(isPerfectSquare(14))
    print(isPerfectSquare(16))
    print(isPerfectSquare(25))
    print(isPerfectSquare(2147483647))
