# runtime: 48.99%, memory usage: 55.85%
def judgeCircle_v1(moves: str) -> bool:
    moves_x, moves_y = 0, 0

    for move in moves:
        if move == 'R':
            moves_x += 1
        elif move == 'L':
            moves_x -= 1
        elif move == 'U':
            moves_y += 1
        else:
            moves_y -= 1

    return moves_x == moves_y == 0


# runtime: 96.35%, memory usage: 94.57%
def judgeCircle_v2(moves: str) -> bool:
    return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')


if __name__ == '__main__':
    print(judgeCircle_v2("UD")) # True
    print(judgeCircle_v2("LL")) # False