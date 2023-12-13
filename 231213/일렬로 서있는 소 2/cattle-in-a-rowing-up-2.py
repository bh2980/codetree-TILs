N = int(input())
cowList = list(map(int, input().split()))

count = 0

for i in range(len(cowList)):
    for j in range(i + 1, len(cowList)):
        for k in range(j + 1, len(cowList)):
            if cowList[i] <= cowList[j] <= cowList[k]:
                count += 1

print(count)