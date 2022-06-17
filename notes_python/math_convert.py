# number conversion
# xyan831

# decimal to base 2, 8, 16
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

# base 2, 8, 16 to decimal
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

# calculate
a = []
a.append(dec_convert(13, 2))
a.append(dec_convert(210, 8))
a.append(dec_convert(501, 16))
a.append(boh_convert(1101, 2))
a.append(boh_convert(322, 8))
a.append(boh_convert('1F5', 16))
print(a)
