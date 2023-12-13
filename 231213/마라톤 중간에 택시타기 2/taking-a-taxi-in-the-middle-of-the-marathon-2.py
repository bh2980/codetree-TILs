N = int(input())
pointList = [list(map(int, input().split())) for _ in range(N)]

def calcDistance(p1, p2):
    r1, c1 = p1
    r2, c2 = p2

    return abs(r1 - r2) + abs(c1 - c2)

import sys

minDis = sys.maxsize

for skip in range(1, N - 1):
    tempDistance = 0
    prevIdx = 0

    for i in range(1, N):
        if i == skip:
            continue

        tempDistance += calcDistance(pointList[prevIdx], pointList[i])
        prevIdx = i

    minDis = min(minDis, tempDistance)

print(minDis)