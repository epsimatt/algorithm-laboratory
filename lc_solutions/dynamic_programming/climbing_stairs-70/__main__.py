to_the_top = [1, 2]


# runtime: 97.77%, memory usage: 60.76%
def climbStairs(n: int) -> int:
    if len(to_the_top) < n:
        to_the_top.insert(n - 1, climbStairs(n - 1) + climbStairs(n - 2))

    return to_the_top[n - 1]


if __name__ == '__main__':
    print(climbStairs(33)) # 5702887
    print(climbStairs(10)) # 89
    print(climbStairs(3)) # 3