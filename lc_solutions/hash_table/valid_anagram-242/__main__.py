# runtime: 99.12%, memory usage: 68.98%
def isAnagram(s: 'str', t: 'str') -> 'bool':
    ls = list(set(s).union(set(t)))

    for e in ls:
        if s.count(e) != t.count(e):
            return False

    return True


if __name__ == '__main__':
    result = isAnagram("anagram", "nagaram")

    print(result)