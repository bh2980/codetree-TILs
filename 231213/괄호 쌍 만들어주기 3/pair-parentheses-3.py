# 첫 번째 여는 괄호를 찾는다
# 그 뒤에서 여는 괄호를 찾는다.
# 찾을 때마다 개수를 추가한다.

parList = input()

count = 0

for i in range(len(parList)):
    par = parList[i]

    if par == '(':
        for j in range(i+1, len(parList)):
            par2 = parList[j]

            if par2 == ")":
                count += 1

print(count)