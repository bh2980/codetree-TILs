N = int(input())
countArr = [int(input()) for _ in range(N)]

minValue = float('inf')

for startIdx in range(len(countArr)):
    tempMin = 0

    for i in range(startIdx, startIdx + len(countArr)):
        tempMin += countArr[i % len(countArr)] * (i - startIdx)

        if tempMin > minValue:
            break

    minValue = min(minValue, tempMin)

print(minValue)