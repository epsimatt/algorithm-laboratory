from typing import List


# runtime: 99.84%, memory usage: 74.72%
def maxArea(height: List[int]) -> int:
    low = 0
    high = len(height) - 1

    result = 0

    while low < high:
        rect_width = high - low

        if height[low] < height[high]:
            rect_height = height[low]
            low += 1
        else:
            rect_height = height[high]
            high -= 1

        if result < rect_width * rect_height:
            result = rect_width * rect_height

    return result


if __name__ == '__main__':
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])) # 49
    print(maxArea([2, 3, 4, 5, 18, 17, 6])) # 17