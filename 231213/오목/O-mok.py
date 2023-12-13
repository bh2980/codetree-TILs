# 좌 하 좌하만 보면 된다.
# 0, 0이 1, 1이 된다/
# 찾으면 시작 좌표, 끝 좌표를 기억해서 /2해서 중간 좌표를 구함.
BOARD = []

while True:
    try:
        line = list(map(int, input().strip().split()))

        BOARD.append(line)
    except:
        break

N = 19

EMPTY = 0

for i in range(N):
    for j in range(N):
        if BOARD[i][j] != EMPTY:
            color = BOARD[i][j]

            try:
                # 가로 확인
                if BOARD[i][j + 1] == color and BOARD[i][j + 2] == color and BOARD[i][j + 3] == color and BOARD[i][j + 4] == color:
                    print(color)
                    print(i + 1, j + 2 + 1)
                    exit(0)
            except:
                try:
                    # 세로 확인
                    if BOARD[i + 1][j] == color and BOARD[i + 2][j] == color and BOARD[i + 3][j] == color and BOARD[i + 4][j] == color:
                        print(color)
                        print(i + 2 + 1, j + 1)
                        exit(0)
                    # 대각선 확인
                    if BOARD[i + 1][j + 1] == color and BOARD[i + 2][j + 2] == color and BOARD[i + 3][j + 3] == color and BOARD[i + 4][j + 4] == color:
                        print(color)
                        print(i + 2 + 1, j + 2 + 1)
                        exit(0)
                except:
                    continue