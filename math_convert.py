# number conversion
# zio800


# decimal to binary
def nc10_2(num10):
    num2 = []
    while num10 / 2 != 0:
        num2.append(str(num10 % 2))
        num10 = num10 // 2
    num2.reverse()
    ans = int(''.join(num2))
    print(ans)


# decimal to octal
def nc10_8(num10):
    num8 = []
    while num10 / 2 != 0:
        num8.append(str(num10 % 8))
        num10 = num10 // 8
    num8.reverse()
    ans = int(''.join(num8))
    print(ans)


# decimal to hexadecimal
def nc10_16(num10):
    hexd = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    num16 = []
    while num10 / 16 != 0:
        num16.append(str(num10 % 16))
        num10 = num10 // 16
    num16.reverse()
    for item in hexd:
        num16 = [hexd[item] if x == item else x for x in num16]
    ans = ''.join(num16)
    print(ans)


# calculate
nc10_2(13)
nc10_8(210)
nc10_16(501)
