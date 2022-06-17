# notes_math
# xyan831

# import module
from math import sqrt, radians, sin, cos
from operator import mul
import numpy as np

# interpolation between 2 points
def interpolation(xi, xlst, ylst):
	yi = ylst[0]+(xi-xlst[0])*((ylst[1]-ylst[0])/(xlst[1]-xlst[0]))
	return yi

# quadratic equation: (a)x + (b)y + (c) = 0
def quad_eq(a, b, c):
	q1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
	q2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
	return [q1, q2]

# magnitude & unit vector: (x, y, z)
def mag_univ(x, y, z):
	mag = sqrt(x**2 + y**2 + z**2)
	univ = [x/mag, y/mag, z/mag]
	return [mag, univ]

# dot & cross product: [(v1*v2), (v1xv2)]
def dot_cross(v1, v2):
	dot = sum(list(map(mul, v1, v2)))
	x = v1[1]*v2[2] - v2[1]*v1[2]
	y = -(v1[0]*v2[2] - v2[0]*v1[2])
	z = v1[0]*v2[1] - v2[0]*v1[1]
	return [dot, [x, y, z]]

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

# normalize a list of numbers to (a, b)
def norm(lst, a=0, b=1):
	newlst = []
	for i in lst:
		new = (i-min(lst))/(max(lst)-min(lst))
		newlst.append((b-a)*new + a)
	return newlst

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