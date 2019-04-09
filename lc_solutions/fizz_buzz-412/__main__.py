from typing import List


# runtime: 80.26%, memory usage: 44.65%
def fizzBuzz(n: 'int') -> 'List[str]':
    result = [str(i) for i in range(1, n + 1)]

    for j in range(1, n + 1):
        if j % 3 == 0 and j % 5 != 0:
            result[j - 1] = "Fizz"
        elif j % 3 != 0 and j % 5 == 0:
            result[j - 1] = "Buzz"
        elif j % 3 == 0 and j % 5 == 0:
            result[j - 1] = "FizzBuzz"
        else:
            continue

    return result

if __name__ == '__main__':
    result = fizzBuzz(15)

    print(result)