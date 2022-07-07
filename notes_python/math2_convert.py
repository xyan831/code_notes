# number conversion
# xyan831

# decimal to base 2, 8, 16
def base10(num10):
	base = [bin(num10), oct(num10), hex(num10)]
	return base

# decimal to base 2, 8, 16 (input integer)
def dec_convert(num, base):
	# for numbers greater than 10
	hexd = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
	con = []
	while num/base != 0:
		con.append(str(num % base))
		num = num // base
	con.reverse()
	for item in hexd:
		con = [hexd[item] if x == item else x for x in con]
	# answer is in string format
	ans = ''.join(con)
	print('base', base, 'number = ', ans)
	return ans

# base 2, 8, 16 to decimal (input string)
def boh_convert(num, base):
	# for numbers greater than 10
	hexd = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
	lenn = [item for item in str(num)]
	lenn.reverse()
	con = []
	for item in hexd:
		lenn = [item if x == hexd[item] else x for x in lenn]
	count = 0
	for i in lenn:
		con.append(int(i) * (base ** count))
		count += 1
	ans = sum(con)
	print('decimal = ', ans)
	return ans