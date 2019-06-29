from typing import List


# time limit exceeded
def maxProfit_v1(prices: List[int]) -> int:
    n = len(prices)
    result = 0

    for i in range(n - 1):
        # k번째 날에 주식을 산다고 가정하면, 최대 수익은 `max(prices[k + 1:]) - prices[k]`가 된다.
        result = max(result, max(prices[(i + 1):]) - prices[i])

    return result


# runtime: 85.18%, memory usage: 93.57%
def maxProfit_v2(prices: List[int]) -> int:
    n = len(prices)

    if n == 0:
        return 0
    else:
        table = [0] * n

        min_price = prices[0]

        for i in range(1, n):
            table[i] = max(table[i - 1], prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return table[n - 1]


if __name__ == '__main__':
    print(maxProfit_v2([1])) # 0
    print(maxProfit_v2([1, 2])) # 2 - 1 = 1
    print(maxProfit_v2([7, 6, 4, 3, 1]))  # 0
    print(maxProfit_v2([7, 1, 5, 3, 6, 4])) # 6 - 1 = 5
