# sliding window

N, K = map(int, input().split())
numList = list(map(int, input().split()))

maxSum = sum(numList[0:K])
tempSum = maxSum

for i in range(K, N):
    prevIdx = i - K

    tempSum -= numList[prevIdx]
    tempSum += numList[i]

    maxSum = max(maxSum, tempSum)

print(maxSum)