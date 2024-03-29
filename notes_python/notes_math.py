# notes_math
# xyan831

# import module
from numpy.linalg import solve
from random import randint
from math import sqrt, radians, sin, cos, factorial
from operator import mul

# roll dices
def roll(dice, face):
	lst = []
	for i in range(dice):
		lst.append(randint(1, face))
	return lst

# interpolation: x=[x1, x2], y=[y1, y2]
def interpolation(xi, x, y):
	p = (y[1]-y[0]) / (x[1]-x[0])
	yi = y[0] + (xi-x[0])*p
	return yi

# quadratic equation: (a)x + (b)y + (c) = 0
def quadratic(a, b, c):
	q1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
	q2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
	return [q1, q2]

# matrix solve linear equation: [a][x] = [b]
def matrixlinear(a, b):
	return solve(a, b)

# phasor: euler's formula e^(i*t) = cos(t) + i*sin(t)
def phasor(a, t):
	r = a*cos(radians(t))
	i = a*sin(radians(t))
	return [r, i]

# class for vector [x, y, z]
class Vector:
	def __init__(self, vec):
		self.vector = vec
		self.mag = sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
		self.univ = self.UV()
	# unit vector
	def UV(self):
		x = self.vector[0]/self.mag
		y = self.vector[1]/self.mag
		z = self.vector[2]/self.mag
		return [x, y, z]
	# dot product
	def DOT(v1, v2):
		return sum(list(map(mul, v1, v2)))
	# cross product
	def CROSS(v1, v2):
		x = v1[1]*v2[2] - v2[1]*v1[2]
		y = -(v1[0]*v2[2] - v2[0]*v1[2])
		z = v1[0]*v2[1] - v2[0]*v1[1]
		return [x, y, z]

# class for number list
class NumList:
	def __init__(self, lst):
		self.lst = lst
		self.max = max(lst)
		self.min = min(lst)
		self.avg = sum(lst)/len(lst)
		self.sd = self.SD()
		self.norm = self.NM()
	# standard deviation
	def SD(self):
		f = []
		for i in self.lst:
			f.append((i-self.avg)**2)
		return (sum(f)/(len(self.lst)-1))**(1/2)
	# normalize list between 2 numbers
	def NM(self, a=0, b=1):
		norm = []
		for i in self.lst:
			new = (i-self.min)/(self.max-self.min)
			norm.append((b-a)*new + a)
		return norm

# class for counting
class Count:
	def __init__(self, n, r):
		self.n = n # elements
		self.r = r # permutations/combinations
		# permutation: P(n, r) = n! / [(n-r)!]
		self.P = factorial(n) / factorial(n-r)
		# permutation with repetition: PR(n, r) = n^r
		self.PR = n**r
		# combination: C(n, r) = n! / [r! * (n-r)!]
		self.C = factorial(n) / (factorial(r)*factorial(n-r))
		# combination with repetition
		# CR(n, r) = C(n-1+r, r) = (n-1+r)! / [r! * (n-1)!]
		self.CR = factorial(n-1+r) / (factorial(r)*factorial(n-1))