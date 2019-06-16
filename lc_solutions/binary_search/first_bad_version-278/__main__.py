# 테스트용 함수
def isBadVersion(version):
    if version >= 4:
        return True
    else:
        return False


def firstBadVersion(n):
    low = 1
    high = n

    while low < high:
        pivot = int((low + high) / 2)

        if isBadVersion(pivot) is True:
            high = pivot
        else:
            low = pivot + 1

    return high


if __name__ == '__main__':
    print(firstBadVersion(5))