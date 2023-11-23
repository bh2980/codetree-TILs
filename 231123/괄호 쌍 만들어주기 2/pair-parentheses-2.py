string = input()

openDict = []
closeDict = []

for i in range(len(string) - 1):
    currentChar = string[i]
    nextChar = string[i + 1]

    if currentChar == nextChar:
        if currentChar == '(':
            openDict.append(i)
        else:
            closeDict.append(i)

answer = 0 

for openIdx in openDict:
    for i in range(len(closeDict)):
        closeIdx = closeDict[i]

        if openIdx + 1 < closeIdx:
            answer += len(closeDict) - i

            break

print(answer)