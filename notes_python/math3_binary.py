# math1: binary solve equation
# xyan831

# import module
from math import sqrt, log

# 4^x + 6^x = 9^x
def check(x):
	lhs = 4**x + 6**x
	rhs = 9**x
	return lhs - rhs

# find x
def solve(left, right):
	mid = (left+right)/2
	result = check(mid)
	if abs(result) <= 0.0001:
		return mid
	else:
		while abs(result) > 0.0001:
			if result > 0:
				left = mid
				mid = (left+right)/2
				result = check(mid)
				if abs(result) <= 0.0001:
					return mid
			elif result < 0:
				right = mid
				mid = (left+right)/2
				result = check(mid)
				if abs(result) <= 0.0001:
					return mid

# calculate
a1 = solve(0, 2)
# solution
a2 = (-1+sqrt(5))/2
print('x =', a1)
print('x =', log(a2, 2/3))
