from typing import List


# runtime: 70.55%, memory usage: 100%
def distributeCandies(candies: int, num_people: int) -> List[int]:
    loop_count, result = 1, [0] * num_people

    while True:
        result[(loop_count - 1) % num_people] += loop_count

        candies -= loop_count
        loop_count += 1

        if candies < loop_count:
            result[(loop_count - 1) % num_people] += candies
            break

    return result


if __name__ == '__main__':
    print(distributeCandies(7, 4)) # [1, 2, 3, 1]
    print(distributeCandies(10, 3)) # [5, 2, 3]
