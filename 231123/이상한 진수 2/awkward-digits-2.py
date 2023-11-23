# 앞에서부터 0을 탐색해서 바꾸고 return
# 없다면 맨 뒤 숫자 0으로 바꿔서 return

def solution(binA):
    for i in range(len(binA)):
        if binA[i] == '0':
            return int('0b' + binA[:i] + '1' + binA[i+1:], 2)

    return int('0b' + binA[:-1] + '0', 2)
        

binA = input()

solution(binA)