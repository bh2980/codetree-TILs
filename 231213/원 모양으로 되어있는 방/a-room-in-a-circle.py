N = int(input())
personList = [int(input()) for _ in range(N)]

import sys

minDis = sys.maxsize

for start in range(len(personList)):
    tempSum = 0

    for i in range(N):
        currentIdx = (start + i) % N

        tempSum += personList[currentIdx] * i
    
    minDis = min(minDis, tempSum)

print(minDis)