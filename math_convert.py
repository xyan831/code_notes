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
    hexd = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
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
    hexd = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
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


# decimal to base 2, 8, 16
def dec_convert(num, base):
    hexd = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    con = []
    while num/base != 0:
        con.append(str(num % base))
        num = num // base
    con.reverse()
    if base == 16:
        for item in hexd:
            con = [hexd[item] if x == item else x for x in con]
    ans = ''.join(con)
    print('base', base, 'number = ', ans)


# base 2, 8, 16 to decimal
def boh_convert(num, base):
    hexd = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    lenn = [item for item in str(num)]
    lenn.reverse()
    con = []
    if base == 16:
        for item in hexd:
            lenn = [item if x == hexd[item] else x for x in lenn]
    count = 0
    for i in lenn:
        con.append(int(i) * (base ** count))
        count += 1
    ans = sum(con)
    print('decimal = ', ans)


# calculate
nc10_2(13)
nc10_8(210)
nc10_16(501)

nc2_10(1101)
nc8_10(322)
nc16_10('1F5')

dec_convert(13, 2)
dec_convert(210, 8)
dec_convert(501, 16)

boh_convert(1101, 2)
boh_convert(322, 8)
boh_convert('1F5', 16)
