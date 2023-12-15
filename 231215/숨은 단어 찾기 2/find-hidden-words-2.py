# LEE의 개수를 구하면 된다.
# 전 8방향으로의 탐색이 필요
# drs, dcs를 활용해서 작성


def inRange(r, c):
    return 0 <= r < N and 0 <= c < M

def exploreLEE(CHAR_LIST, current, diff, length = 1):
    cr, cc = current
    dr, dc = diff

    nr, nc = cr + dr, cc + dc

    if length == 3:
        return True

    if not inRange(nr, nc):
        return False

    if CHAR_LIST[nr][nc] == 'E':
        return exploreLEE(CHAR_LIST, (nr, nc), diff, length + 1)

    return False

def solution(CHAR_LIST):
    count = 0

    drs = [0, -1, 0, 1, -1, -1, 1, 1]
    dcs = [-1, 0, 1, 0, -1, 1, -1, 1]

    for i in range(N):
        for j in range(M):
            # i, j를 시작으로 하는 것
            if CHAR_LIST[i][j] == 'L':
                for diff in zip(drs, dcs):
                   if exploreLEE(CHAR_LIST, (i, j), diff, 1):
                    count += 1

    return count

N, M = map(int, input().split())
CHAR_LIST = [list(input()) for _ in range(N)]

print(solution(CHAR_LIST))