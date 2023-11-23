N, target = map(int, input().split())
numArr = list(map(int, input().split()))

minDiff = float('inf')

for skipIdx1 in range(len(numArr)):
    for skipIdx2 in range(skipIdx1 + 1, len(numArr)):
        tempSum = 0

        for idx in range(len(numArr)):
            if idx != skipIdx1 and idx != skipIdx2:
                tempSum += numArr[idx]

        minDiff = min(abs(tempSum - target), minDiff)

print(minDiff)