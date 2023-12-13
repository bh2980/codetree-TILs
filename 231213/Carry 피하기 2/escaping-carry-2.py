# 뒤의 숫자부터 더해가면서 앞의 숫자까지 옴.
# 뒤의 숫자를 더할 때 carry가 생기면 그만하고 pass
# 모든 과정애소 carry가 없다면 최댓값 업데이트

maxValue = 0

N = int(input())
numList = [int(input()) for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            # carry가 없음을 검증
            
            numA = numList[i]
            numB = numList[j]
            numC = numList[k]

            isCarry = False

            while numA != 0 and numB != 0 and numC != 0:
                numA, leftA = divmod(numA, 10)
                numB, leftB = divmod(numB, 10)
                numC, leftC = divmod(numC, 10)

                if leftA + leftB + leftC >= 10:
                    isCarry = True
                    break
            # 더하기

            if not isCarry:
                maxValue = max(maxValue, numList[i] + numList[j] + numList[k])

print(maxValue)