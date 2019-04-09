# runtime: 100.00%, memory usage: 75.00%
def findTheDifference(s: 'str', t: 'str') -> 'str':
    for c in t:
        if s.count(c) != t.count(c):
            return c


if __name__ == '__main__':
    result = findTheDifference("abcd", "abcde")

    print(result)