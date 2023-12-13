parStr = input()

count = 0

for i in range(1, len(parStr)):
    par1 = parStr[i-1]
    par2 = parStr[i]

    if par1 == "(" and par2 == '(':
        for j in range(i + 1, len(parStr)):
            par3 = parStr[j-1]
            par4 = parStr[j]

            if par3 == ')' and par4 == ')':
                count += 1

print(count)