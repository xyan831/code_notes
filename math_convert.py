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
    print('binary = ', ans)


# decimal to octal
def nc10_8(num10):
    num8 = []
    while num10 / 2 != 0:
        num8.append(str(num10 % 8))
        num10 = num10 // 8
    num8.reverse()
    ans = int(''.join(num8))
    print('octal = ', ans)


# decimal to hexadecimal
def nc10_16(num10):
    hexd = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f'}
    num16 = []
    while num10 / 16 != 0:
        num16.append(str(num10 % 16))
        num10 = num10 // 16
    num16.reverse()
    for item in hexd:
        num16 = [hexd[item] if x == item else x for x in num16]
    ans = ''.join(num16)
    print('hexadecimal = ', ans)


# binary to decimal
def nc2_10(num2):
    lenn = [item for item in str(num2)]
    lenn.reverse()
    num10 = []
    count = 0
    for i in lenn:
        num10.append(int(i) * (2 ** count))
        count += 1
    ans = sum(num10)
    print('decimal = ', ans)


# octal to decimal
def nc8_10(num8):
    lenn = [item for item in str(num8)]
    lenn.reverse()
    num10 = []
    count = 0
    for i in lenn:
        num10.append(int(i) * (8 ** count))
        count += 1
    ans = sum(num10)
    print('decimal = ', ans)


# hexadecimal to decimal
def nc16_10(num16):
    hexd = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f'}
    lenn = [item for item in str(num16)]
    lenn.reverse()
    lenn2 = []
    for item in hexd:
        lenn2 = [item if x == hexd[item] else x for x in lenn]
    num10 = []
    count = 0
    for i in lenn2:
        num10.append(int(i) * (16 ** count))
        count += 1
    ans = sum(num10)
    print('decimal = ', ans)


# calculate
nc10_2(13)
nc10_8(210)
nc10_16(501)

nc2_10(1101)
nc8_10(322)
nc16_10('1f5')
