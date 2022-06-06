# math1: binary solve equation
# xyan831

# import module
from math import sqrt, log

# 4^x + 6^x = 9^x
def check(x):
	global result
	lhs = (4**x) + (6**x)
	rhs = 9**x
	result = lhs - rhs

# find x
result = 0
a = 0
b = 2
c = (a+b)/2
check(c)

if abs(result) <= 0.0001:
	print('x = ', c)
else:
	while abs(result) > 0.0001:
		if result > 0:
			a = c
			c = (a+b)/2
			check(c)
			if abs(result) <= 0.0001:
				print('x = ', c)
				break
		if result < 0:
			b = c
			c = (a+b)/2
			check(c)
			if abs(result) <= 0.0001:
				print('x = ', c)
				break

# solution equation
a = (-1+sqrt(5))/2
print('x = ', log(a, 2/3))
