# 합이 최소
import sys

N = int(input())
arr = list(map(int, input().split()))

minSum = sys.maxsize

for i in range(N):
    tempSum = 0

    for j in range(N):
        tempSum += abs(i - j) * arr[j]

    minSum = min(minSum, tempSum)

print(minSum)