# notes_math
# zio800

from math import *
from operator import *
import numpy as np


# quadratic equation: (qa)x + (qb)y + (qc) = 0
def quad_eq(qa, qb, qc):
    global qe1
    global qe2
    qe1 = ((-qb) + sqrt((qb ** 2) - (4 * qa * qc))) / (2 * qa)
    qe2 = ((-qb) - sqrt((qb ** 2) - (4 * qa * qc))) / (2 * qa)
    print('quadratic equation (+):\n', qe1)
    print('quadratic equation (-):\n', qe2)


# magnitude & unit vector: [vx, vy, vz]
def mag_univ(vx, vy, vz):
    global univ
    mag = sqrt(vx**2 + vy**2 + vz**2)
    univ = [vx/mag, vy/mag, vz/mag]
    print('magnitude:\n', mag)
    print('unit vector:\n', univ)


# dot & cross product: (v1 * v2), (v1 x v2)
def dot_cross(v1, v2):
    dot_pro = sum(list(map(mul, v1, v2)))
    print('dot product:\n', dot_pro)
    x = v1[1]*v2[2] - v2[1]*v1[2]
    y = -(v1[0]*v2[2] - v2[0]*v1[2])
    z = v1[0]*v2[1] - v2[0]*v1[1]
    cross_pro = [x, y, z]
    print('cross product:\n', cross_pro)


# matrix solve linear equation
def mat_lin(na, nb):
    global lin_eq
    lin_eq = np.linalg.solve(na, nb)
    print('solution:\n', lin_eq)


# average and standard deviation
def avg_sd(lst):
    global avg
    global sd
    s = sum(lst)
    n = len(lst)
    avg = s/n
    f = []
    for i in lst:
        f.append((i-avg)**2)
    sd = (sum(f)/(n-1))**(1/2)
    print('average = ', avg)
    print('standard deviation = ', sd)
    print('upper : lower error = ', avg+sd, ':', avg-sd)


# phasor: euler's formula e^(i*theta) = cos(theta) + i*sin(theta)
def phasor(a, t):
    global r
    global i
    th = radians(t)
    r = a*cos(th)
    i = a*sin(th)
    print('ans = ', r, '+ j', i)


# calculate
quad_eq(4, 1, -3)

mag_univ(-1, 1.5, 2)

va = [-7, 0.4+5.25, 0]
vb = [-3, -12, 4]
dot_cross(va, vb)

lin_a = np.array([[1, 1.9], [1, 5.8]])
lin_b = np.array([49.4, 99.3])
mat_lin(lin_a, lin_b)

l1 = [520, 512, 515, 522]
avg_sd(l1)

phasor(14.54, 9.90)
