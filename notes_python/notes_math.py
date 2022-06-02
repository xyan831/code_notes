# notes_math
# xyan831

from math import sqrt, radians, sin, cos
from operator import mul
import numpy as np

# interpolation
def interpolation(xi, x, y):
	yi = y[0] + (xi-x[0])*((y[1]-y[0])/(x[1]-x[0]))
	print('y = ', yi)
	return yi

# quadratic equation: (qa)x + (qb)y + (qc) = 0
def quad_eq(qa, qb, qc):
	qe1 = ((-qb) + sqrt((qb ** 2) - (4 * qa * qc))) / (2 * qa)
	qe2 = ((-qb) - sqrt((qb ** 2) - (4 * qa * qc))) / (2 * qa)
	qe = [qe1, qe2]
	print('quadratic equation (+):\n', qe1)
	print('quadratic equation (-):\n', qe2)
	return qe

# magnitude & unit vector: [vx, vy, vz]
def mag_univ(vx, vy, vz):
	global mag
	mag = sqrt(vx**2 + vy**2 + vz**2)
	univ = [vx/mag, vy/mag, vz/mag]
	print('magnitude:\n', mag)
	print('unit vector:\n', univ)
	return univ

# dot & cross product: (v1 * v2), (v1 x v2)
def dot_cross(v1, v2):
	global dot
	dot = sum(list(map(mul, v1, v2)))
	print('dot product:\n', dot)
	x = v1[1]*v2[2] - v2[1]*v1[2]
	y = -(v1[0]*v2[2] - v2[0]*v1[2])
	z = v1[0]*v2[1] - v2[0]*v1[1]
	cross = [x, y, z]
	print('cross product:\n', cross)
	return cross

# matrix solve linear equation
def mat_lin(na, nb):
	lin_eq = np.linalg.solve(na, nb)
	print('solution:\n', lin_eq)
	return lin_eq

# average and standard deviation
def avg_sd(lst):
	avg = sum(lst)/len(lst)
	f = []
	for i in lst:
		f.append((i-avg)**2)
	sd = (sum(f)/(len(lst)-1))**(1/2)
	ad = [avg, sd]
	print('average = ', avg)
	print('standard deviation = ', sd)
	print('upper : lower error = ', avg+sd, ':', avg-sd)
	return ad

# decimal to base 2, 8, 16
def base10(num10):
	base = [bin(num10), oct(num10), hex(num10)]
	print(int(base[0], 2), '(binary) = ', base[0])
	print(int(base[1], 8), '(octal) = ', base[1])
	print(int(base[2], 16), '(hexadecimal) = ', base[2])
	return base

# phasor: euler's formula e^(i*theta) = cos(theta) + i*sin(theta)
def phasor(a, t):
	th = radians(t)
	r = a*cos(th)
	i = a*sin(th)
	cn = [r, i]
	print('ans = ', r, '+ j', i)
	return cn

# calculate
xi = 0.495
x = [0.4949, 0.4951]
y = [2.57, 2.58]
yi = interpolation(xi, x, y)

a1 = quad_eq(4, 1, -3)

a2 = mag_univ(-1, 1.5, 2)

va = [-7, 0.4+5.25, 0]
vb = [-3, -12, 4]
a3 = dot_cross(va, vb)

lin_a = np.array([[1, 1.9], [1, 5.8]])
lin_b = np.array([49.4, 99.3])
a4 = mat_lin(lin_a, lin_b)

l1 = [520, 512, 515, 522]
a5 = avg_sd(l1)

a6 = base10(79)

a7 = phasor(14.54, 9.90)
