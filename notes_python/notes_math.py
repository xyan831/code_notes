# notes_math
# xyan831

# import module
from math import sqrt, radians, sin, cos
from operator import mul
import numpy as np

# interpolation
def interpolation(xi, x, y):
	yi = y[0] + (xi-x[0])*((y[1]-y[0])/(x[1]-x[0]))
	return yi

# quadratic equation: (a)x + (b)y + (c) = 0
def quad_eq(a, b, c):
	q1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
	q2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
	return [q1, q2]

# magnitude & unit vector: [x, y, z]
def mag_univ(x, y, z):
	mag = sqrt(x**2 + y**2 + z**2)
	univ = [x/mag, y/mag, z/mag]
	return [mag, univ]

# dot & cross product: (v1 * v2), (v1 x v2)
def dot_cross(v1, v2):
	dot = sum(list(map(mul, v1, v2)))
	x = v1[1]*v2[2] - v2[1]*v1[2]
	y = -(v1[0]*v2[2] - v2[0]*v1[2])
	z = v1[0]*v2[1] - v2[0]*v1[1]
	cross = [x, y, z]
	return [dot, cross]

# matrix solve linear equation
def mat_lin(na, nb):
	lin_eq = np.linalg.solve(na, nb)
	return lin_eq

# average and standard deviation
def avg_sd(lst):
	avg = sum(lst)/len(lst)
	f = []
	for i in lst:
		f.append((i-avg)**2)
	sd = (sum(f)/(len(lst)-1))**(1/2)
	return [avg, sd]

# decimal to base 2, 8, 16
def base10(num10):
	base = [bin(num10), oct(num10), hex(num10)]
	return base

# phasor: euler's formula e^(i*theta) = cos(theta) + i*sin(theta)
def phasor(a, t):
	th = radians(t)
	r = a*cos(th)
	i = a*sin(th)
	cn = [r, i]
	return cn

# calculate
xi = 0.495
x = [0.4949, 0.4951]
y = [2.57, 2.58]
yi = interpolation(xi, x, y)
print('interpolation y:', yi)

a1 = quad_eq(4, 1, -3)
print('quadratic eq:', a1)
a2 = mag_univ(-1, 1.5, 2)
print('magnitude:', a2[0], '\nunit vector:', a2[1])

va = [-7, 0.4+5.25, 0]
vb = [-3, -12, 4]
a3 = dot_cross(va, vb)
print('dot:', a3[0], '\ncross', a3[1])

lin_a = np.array([[1, 1.9],
				  [1, 5.8]])
lin_b = np.array([49.4, 99.3])
a4 = mat_lin(lin_a, lin_b)
print('matrix lin solution:', a4)

a5 = avg_sd([520, 512, 515, 522])
print('avg:', a5[0], '\nstandard dev:', a5[1])
print('upper : lower error:', a5[0]+a5[1], ":", a5[0]-a5[1])
a6 = base10(79)
print('binary:', a6[0], '\noctal:', a6[1], '\nhexadecimal:', a6[2])
a7 = phasor(14.54, 9.90)
print('phasor:', a7[0], '+ j', a7[1])
