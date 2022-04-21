from math import radians, sin, cos
import numpy as np
# index
K = 10**3 # kilo
M = 10**6 # mega
G = 10**9 # giga
# material properties
E11 = 20.01*M
E22 = 1.3*M
G12 = 1.03*M
v12 = 0.3
v21 = 0.019
# constants [A = W*N*pt]
Er = 10*M
pt = 0.005
# configs
c1 = [45, 90, -45, 45, -45, 0, 0]
c2 = [45, 90, -45, 45, -45, 45, -45]
c3 = [45, 90, -45, 45, -45, 0, 0]
C = [c1+list(reversed(c1)), c2+list(reversed(c2)), c3+list(reversed(c3))]

def T1(th): # stress local to global
    T1 = np.array([[cos(th)**2, sin(th)**2, 2*sin(th)*cos(th)],
                   [sin(th)**2, cos(th)**2, -2*sin(th)*cos(th)],
                   [-sin(th)*cos(th), sin(th)*cos(th), cos(th)**2-sin(th)**2]])
    return T1
def T2(th): # strain local to global
    T2 = np.array([[cos(th)**2, sin(th)**2, sin(th)*cos(th)],
                   [sin(th)**2, cos(th)**2, -sin(th)*cos(th)],
                   [-2*sin(th)*cos(th), 2*sin(th)*cos(th), cos(th)**2-sin(th)**2]])
    return T2
def Q1(E11, E22, G12, v12, v21): # local stress to strain
    Q1 = np.array([[E11/(1-v12*v21), v12*E22/(1-v12*v21), 0],
                   [v21*E11/(1-v12*v21), E22/(1-v12*v21), 0],
                   [0, 0, G12]])
    return Q1
def Q2(Q1, T1, T2): # global stress to strain
    return np.linalg.inv(T1) @ Q1 @ T2
def make(Q1, x, y, N, config, pt):
    a = 0
    for i in range(1, N+1):
        Q = Q2(Q1, T1(radians(config[i-1])), T2(radians(config[i-1])))
        zk = pt*(i - N/2)
        zk1 = pt*(i-1 - N/2)
        a += Q[x][y]*(zk-zk1)
    return a
Q1 = Q1(E11, E22, G12, v12, v21)
# global
Exx = []
Gxy = []
for i in range(0, len(C)):
    N = len(C[i])
    A1 = np.array([[make(Q1, 0, 0, N, C[i], pt), make(Q1, 0, 1, N, C[i], pt), 0],
                   [make(Q1, 1, 0, N, C[i], pt), make(Q1, 1, 1, N, C[i], pt), 0],
                   [0, 0, make(Q1, 2, 2, N, C[i], pt)]]) # balanced
    Exx.append((A1[0][0]/(N*pt))*(1-(A1[0][1]**2)/(A1[0][0]*A1[1][1])))
    Gxy.append(A1[2][2]/(N*pt))
        
# flange
p = 20000
M = 5000
V = 1000
exxc = 0.004
yxyc = 0.007
W = [2, 2, 2]
h = [pt*len(C[0]), pt*len(C[1]), pt*len(C[2])]
y = [h[2]+W[1]+h[0]/2, h[2]+W[1]/2, h[2]/2]

# calculate
A = []
A_ = 0
y_1 = 0
y_2 = 0
for i in range(0, len(W)):
    A.append(W[i]*len(C[i])*pt)
    A_ += Exx[i]*A[i]/Er
    y_1 += y[i]*A[i]*Exx[i]
    y_2 += A[i]*Exx[i]

y_ = y_1/y_2
I = [(W[0]*h[0]**3/12)+A[0]*h[0]**2, (h[1]*W[1]**3/12)+A[1]*h[1]**2, (W[2]*h[2]**3/12)+A[2]*h[2]**2]

I_ = 0
P = []
#Nxx = []
Nxxc = []
Nxyc = []
Pc = 0
for i in range(0, len(W)):
    I_ += I[i]*Exx[i]/Er
    P.append(p*A[i]/(Er*A_/Exx[i]))
    #Nxx.append(P[i]/W[i])
    Nxxc.append(Exx[i]*exxc*h[i])
    Nxyc.append(Gxy[i]*yxyc*h[i])
    Pc += Nxxc[i]*W[i]

Nxxf = (Exx[0]/Er)*(M*(y[0]-y_)/I_)*h[i]
Qf = (Exx[0]/Er)*(W[0]+h[1]/2)*(h[0]*W[1]/2)
Nxyf = V*Qf/I_
Qw = Qf + (Exx[1]/Er)*(W[1]/4)*(h[1]*W[1]/2)
Nxyw = V*Qw/I_
'''
print('A: ', A)
print('I: ', I)
print('Exx: ', Exx)
print('A_: ', A_)
print('I_: ', I_)
print('P: ', P)
print('y_: ', y_)
print('Nxx: ', Nxx)
print('Nxxc: ', Nxxc)

print(I_)
print(Exx[0])
print(Nxxc[0])
print(Nxxf)
print(Nxxc[0]/Nxxf)
print(Qw)
print(Gxy[0])
print(Nxyc[0])
print(Nxyw)
print(Nxyc[0]/Nxyw)
'''
print(Nxxf, Nxyf, Nxyw)