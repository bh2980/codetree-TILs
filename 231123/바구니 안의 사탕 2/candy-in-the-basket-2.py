N, K = map(int, input().split())

candyDict = dict()

maxPos = -1

for _ in range(N):
    candyCount, basket = map(int, input().split())

    try:
        temp = candyDict[basket]

        candyDict[basket] += candyCount
    except:
        candyDict[basket] = candyCount

    maxPos = max(maxPos, basket)

candyList = [0 for _ in range(maxPos + 1)]

for idx, value in candyDict.items():
    candyList[idx] = value

maxCount = 0

for idx in range(len(candyList)):
    maxCount = max(sum(candyList[idx - K : idx + K + 1]), maxCount)

print(maxCount)