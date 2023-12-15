import sys

INF = sys.maxsize

N, S = map(int, input().split())
arr = list(map(int, input().split()))

minDiff = INF

for skip1 in range(N):
    for skip2 in range(skip1 + 1, N):
        tmpSum = 0

        for i in range(N):
            if i == skip1 or i == skip2:
                continue

            tmpSum += arr[i]

        minDiff = min(minDiff, abs(tmpSum - S))

print(minDiff)