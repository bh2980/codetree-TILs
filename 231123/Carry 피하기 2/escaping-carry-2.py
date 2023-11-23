def combinations(_list, count):
    if count == 1:
        return [[item] for item in _list]
    
    list_arr = []

    for fixIdx in range(len(_list)):
        fixElement = _list[fixIdx]

        for combi in combinations(_list[fixIdx+1:], count - 1):
            list_arr.append([fixElement] + combi)


    return list_arr

N = int(input())
numArr = sorted(list(int(input()) for _ in range(N)))

maxSumValue = -1

for combi in combinations(numArr, 3):
    tempSum = 0
    carry = False
    
    for num in combi:
        maxLength = len(str(max(num, tempSum)))

        tempStrSum = str(tempSum).rjust(maxLength, '0')
        numStr = str(num).rjust(maxLength, '0')

        for idx in range(maxLength):
            if int(tempStrSum[idx]) + int(numStr[idx]) >= 10:
                carry = True
                break
        
        if carry:
            break

        tempSum += num

    if not carry:
        maxSumValue = max(maxSumValue, tempSum)

print(maxSumValue)