from typing import List


# runtime: 67.06%, memory usage: 8.33%
def isRectangleOverlap(rec1: List[int], rec2: List[int]) -> bool:
    rec1_x1, rec1_y1, rec1_x2, rec1_y2 = rec1[0], rec1[1], rec1[2], rec1[3]
    rec2_x1, rec2_y1, rec2_x2, rec2_y2 = rec2[0], rec2[1], rec2[2], rec2[3]

    return rec2_x1 < rec1_x2 and rec2_x2 > rec1_x1 and rec2_y1 < rec1_y2 and rec2_y2 > rec1_y1


if __name__ == '__main__':
    print(isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3])) # True
    print(isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1])) # False
    print(isRectangleOverlap([7, 8, 13, 15], [10, 8, 12, 20])) # True
    print(isRectangleOverlap([2, 17, 6, 20], [3, 8, 6, 20])) # True
    print(isRectangleOverlap([4, 4, 14, 7], [4, 3, 8, 8])) # True
