# 왼쪽 상단에서 우측 하단으로 이동
# 시작 - 1 - 2 - 끝을 만족해야함
# 오른쪽 아래로만 이동 가능

WHITE = 'W'
BLACK = 'B'

def reverseTile(tile):
    return WHITE if tile == BLACK else BLACK

N, M = map(int, input().split())
MAP = [input().split() for _ in range(N)]

startTile = MAP[0][0]
endTile = MAP[N-1][M-1]

count = 0

for i in range(1, N - 1):
    for j in range(1, M - 1):
        if MAP[i][j] == reverseTile(startTile):
            for i_2 in range(i + 1, N - 1):
                for j_2 in range(j + 1, M - 1):
                    if MAP[i_2][j_2] == reverseTile(endTile):
                        count += 1

print(count)