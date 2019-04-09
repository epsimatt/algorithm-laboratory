from typing import List


# runtime: 93.54%, memory usage: 47.90%
def reverseString(s: 'List[str]') -> 'None':
    """
    Do not return anything, modify s in-place instead.
    """
    le = len(s) - 1

    for i in range(0, int((le + 1) / 2)):
        t = s[le - i]
        s[le - i] = s[i]
        s[i] = t


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)

    print(s)