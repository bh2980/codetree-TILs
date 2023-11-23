N, H, T = map(int, input().split())
land = list(map(int, input().split()))

minAnswer = float('inf')

for i in range(len(land) - T + 1):
    tempAnswer = 0

    for h in land[i:i + T]:
        tempAnswer += abs(h - H)

    minAnswer = min(minAnswer, tempAnswer)

print(minAnswer)