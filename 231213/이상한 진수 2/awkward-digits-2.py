binStr = list(input())

# 앞에서부터 탐색해서 0이 보이면 그걸 바꾼다
# 0이 없다면 가장 뒤에 것을 바꾼다.

for i in range(len(binStr)):
    if binStr[i] == '0':
        binStr[i] = '1'
        print(int(''.join(binStr), 2))
        exit(0)

binStr[len(binStr) - 1] = '0'
print(int(''.join(binStr), 2))