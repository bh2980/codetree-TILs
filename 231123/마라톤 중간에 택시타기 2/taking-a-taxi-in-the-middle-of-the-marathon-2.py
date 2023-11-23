def calcTaxiDistance(plist):
    accTaxi = 0

    for i in range(len(plist) - 1):
        nextIdx = i + 1;

        x1, y1 = plist[i]
        x2, y2 = plist[nextIdx]

        accTaxi += abs(x1 - x2) + abs(y1 - y2)

    return accTaxi

def solution(N, pointList):
    minValue = float('inf')

    for skip in range(1, N):
        minValue = min(calcTaxiDistance(pointList[:skip] + pointList[skip+1:]), minValue)


    return minValue

N = int(input())
pointList = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, pointList))