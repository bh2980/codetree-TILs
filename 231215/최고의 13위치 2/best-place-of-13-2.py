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

        for nsi in range(si, N):
            for nsj in range(sj + 1 if nsi == si else 0, N):
                nei, nej = nsi, nsj + 2

                if not inRange(nei, nej):
                    continue

                # print((si, sj), (ei, ej), '/', (nsi, nsj), (nei, nej))
                maxCount = max(maxCount, sum(MAP[si][sj:ej + 1]) + sum(MAP[nsi][nsj:nej + 1]))

print(maxCount)