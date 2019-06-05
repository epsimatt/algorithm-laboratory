if __name__ == '__main__':
    # 입력값
    N = int(input())

    if not N & 1:
        raise SystemExit('error: input must be an odd number')

    if N is 1:
        print(1)
    else:
        # 결과 배열
        result = [x[:] for x in [[1] * N] * N]

        # y, x좌표의 값
        R = int((N - 1) / 2)

        # 현재 y, x좌표
        y, x = R, R

        # 총 이동 횟수
        total_moves = 0

        # 다음 이동 횟수
        next_moves = 0

        # 다음 칸에 나와야 될 숫자
        current = 1

        while result[N - 1][0] == 1:
            # 이동 방향
            direction = total_moves % 4

            # 왼쪽으로 이동
            if direction == 0:
                for i in range(next_moves):
                    x -= 1
                    result[y][x] = current + 1
                    current += 1

            # 아래쪽으로 이동
            elif direction == 1:
                for i in range(next_moves):
                    y += 1
                    result[y][x] = current + 1
                    current += 1

            # 오른쪽으로 이동
            elif direction == 2:
                for i in range(next_moves):
                    x += 1
                    result[y][x] = current + 1
                    current += 1

            # 위쪽으로 이동
            elif direction == 3:
                for i in range(next_moves):
                    y -= 1
                    result[y][x] = current + 1
                    current += 1

            # 다음 이동 횟수 증가
            if result[0][0] == 1 and not total_moves & 1:
                next_moves += 1

            # 총 이동 횟수 증가
            total_moves += 1

        width = len(str(N * N))

        # 배열의 모든 원소 하나씩 출력
        for y in range(N):
            for x in range(N):
                # 배열 오른쪽 정렬
                print(str(result[y][x]).rjust(width), end=' ')

            print()