# notes_math
# xyan831

# import module
import numpy as np
import random as rd
from math import sqrt, radians, sin, cos
from operator import mul

# roll dices
def roll(dice, face):
	lst = []
	for i in range(dice):
		lst.append(rd.randint(1, face))
	return lst

# interpolation between 2 points
def interpolation(xi, xlst, ylst):
	p = (ylst[1]-ylst[0]) / (xlst[1]-xlst[0])
	yi = ylst[0] + (xi-xlst[0])*p
	return yi

# quadratic equation: (a)x + (b)y + (c) = 0
def quad_eq(a, b, c):
	q1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
	q2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
	return [q1, q2]

# matrix solve linear equation: [a][x] = [b]
def mat_lin(a, b):
	x = np.linalg.solve(a, b)
	return x

# phasor: euler's formula e^(i*theta) = cos(theta) + i*sin(theta)
def phasor(a, t):
	th = radians(t)
	r = a*cos(th)
	i = a*sin(th)
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
