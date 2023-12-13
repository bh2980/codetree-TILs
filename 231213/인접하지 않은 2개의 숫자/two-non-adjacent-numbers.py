N = int(input())
numArr = list(map(int, input().split()))

maxSum = 0

for i in range(N):
    for j in range(i + 2, N):
        maxSum = max(maxSum, numArr[i] + numArr[j])

print(maxSum)