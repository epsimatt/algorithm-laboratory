# runtime: 100.00%, memory usage: 15.19%
def reverseWords(s: 'str') -> 'str':
    result = []

    for word in s.split(' '):
        result.append(word[::-1])

    return ' '.join(result)

if __name__ == '__main__':
    result = reverseWords("Let's take LeetCode contest")

    print(result)