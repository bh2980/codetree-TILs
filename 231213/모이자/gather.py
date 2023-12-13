N = int(input())
numList = list(map(int, input().split()))

maxResult = 0

for i in range(N):
    numList[i] *= 2

    tempSum = 0

    for j in range(N - 1):
        tempSum += abs(numList[j] - numList[j+1])

    numList[i] //= 2

    maxResult = max(maxResult, tempSum)


print(maxResult)