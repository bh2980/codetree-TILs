count = 0

N = int(input())
arr = list(map(int, input().split()))

for s in range(N):
    for e in range(s + 1, N + 1):
        avg = sum(arr[s:e]) / (e - s)

        if avg in arr[s:e]:
            count += 1

print(count)