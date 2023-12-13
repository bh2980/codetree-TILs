N = int(input())
pointList = [list(map(int, input().split())) for _ in range(N)]

def calcDistance(p1, p2):
    r1, c1 = p1
    r2, c2 = p2

    return abs(r1 - r2) + abs(c1 - c2)

import sys

minDis = sys.maxsize

for skip in range(1, len(pointList) - 1):
    skippedArr = pointList[:skip] + pointList[skip + 1:]

    tempDistance = 0

    for i in range(len(skippedArr) - 1):
        tempDistance += calcDistance(skippedArr[i], skippedArr[i + 1])

    minDis = min(minDis, tempDistance)

print(minDis)