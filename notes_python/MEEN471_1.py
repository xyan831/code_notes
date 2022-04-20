#from math import radians, sin, cos
#import numpy as np

# index
K = 10**3 # kilo
M = 10**6 # mega
G = 10**9 # giga
# constants [A = W*N*pt]
Er = 10
pt = 0.005
# config
c1 = [0]*4 + [45] + [0]*3 + [-45, 90]
c2 = [0] + [45, -45]*2 + [0] + [45, -45]*2
c3 = [0]*2 + [45, -45] + [0]*2 + [45, -45]*2
C = [c1+list(reversed(c1)), c2+list(reversed(c2)), c3+list(reversed(c3))]
# flange
p = 20000
exxc = 0.004
W = [3, 3.5, 2]
y = [3.65, 1.85, 0.05]
A = []
Exx = [19.79*M, 8.219*M, 12.8*M]
A_ = 0
y_1 = 0
y_2 = 0
for i in range(0, len(W)):
    A.append(W[i]*len(C[i])*pt)
    A_ += Exx[i]*A[i]/Er
    y_1 += y[i]*A[i]*Exx[i]
    y_2 += A[i]*Exx[i]
y_ = y_1/y_2
P = []
Nxx = []
Nxxc = []
Pc = 0
for i in range(0, len(W)):
    P.append(p*A[i]/(Er*A_/Exx[i]))
    Nxx.append(P[i]/W[i])
    Nxxc.append(Exx[i]*exxc*len(C[i])*pt)
    Pc += Nxxc[i]*W[i]

print('A: ', A)
print('Exx: ', Exx)
print('A_: ', A_)
print('P: ', P)
print('y_: ', y_)
print('Nxx: ', Nxx)
print('Nxxc: ', Nxxc)
