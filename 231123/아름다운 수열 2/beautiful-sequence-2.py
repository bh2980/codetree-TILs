N , M = map(int, input().split())
AList = list(map(int, input().split()))
BList = sorted(list(map(int, input().split())))
count = 0

for i in range(len(AList) - len(BList) + 1):
    if BList == sorted(AList[i:i+len(BList)]):
        count += 1

print(count)