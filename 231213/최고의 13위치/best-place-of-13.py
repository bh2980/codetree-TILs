N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

maxCount = 0

for i in range(N):
    for j in range(N - 2):
        tempCount = 0

        box1 = arr[i][j]
        box2 = arr[i][j + 1]
        box3 = arr[i][j + 2]

        if box1 == 1:
            tempCount += 1
        
        if box2 == 1:
            tempCount += 1
        
        if box3 == 1:
            tempCount += 1

        maxCount = max(maxCount, tempCount)

print(maxCount)