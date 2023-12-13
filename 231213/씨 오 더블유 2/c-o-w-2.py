N = int(input())
COWSTR = input()

count = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if COWSTR[i] == 'C' and COWSTR[j] == 'O' and COWSTR[k] == 'W':
                count += 1

print(count)