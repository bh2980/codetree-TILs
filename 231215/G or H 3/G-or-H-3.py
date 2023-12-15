N, K = map(int, input().split())
numList = []
maxCount = 0

for _ in range(N):
    idx, alpha = input().split()
    idx = int(idx)

    maxCount = max(idx, maxCount)

    numList.append((idx - 1, 1 if alpha == 'G' else 2))

arr = [0 for _ in range(maxCount)]

for idx, alpha in numList:
    arr[idx] = alpha

maxSum = sum(arr[:K + 1])
tempSum = maxSum

for i in range(K + 1, N):
    previdx = i - (K + 1)

    tempSum -= arr[previdx]
    tempSum += arr[i]

    maxSum = max(maxSum, tempSum)

print(maxSum)