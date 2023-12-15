N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

def inRange(r, c):
    return 0 <= r < N and 0 <= c < N

maxCount = 0

for si in range(N):
    for sj in range(N):
        ei, ej = si, sj + 2

        if not inRange(ei, ej):
            continue

        nsi, nsj = [ei, ej + 1] if ej + 1 < N else [ei + 1, 0]
        nei, nej = nsi, nsj + 2

        if not inRange(nei, nej):
            continue

        maxCount = max(maxCount, sum(MAP[si][sj:ej + 1]) + sum(MAP[nsi][nsj:nej + 1]))

print(maxCount)