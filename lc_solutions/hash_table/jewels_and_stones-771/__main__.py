# runtime: 99.66%, memory usage: 50.13%
def numJewelsInStones(J: 'str', S: 'str') -> 'int':
    result = 0

    for c in set(J):
        result += S.count(c)

    return result

if __name__ == '__main__':
    result = numJewelsInStones("aA", "aAAbbbb")

    print(result)