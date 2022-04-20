from math import radians, sin, cos
import numpy as np
# index
K = 10**3 # kilo
M = 10**6 # mega
G = 10**9 # giga
# material properties
E11 = 26.25*M
E22 = 1.49*M
G12 = 1.04*M
v12 = 0.28
v21 = 0.016
# laminate config [0, 45/-45, 90]
c = [0]*12 + [45]*3 + [-45]*3 + [90]*2
config = c + list(reversed(c))
N = len(config)
pt = 0.005
# strain allowables
ec = 0.0035
yc = 0.004
Nxxc = 8000
Nxyc = 1300

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
A = np.array([[make(Q1, 0, 0, N, config, pt), make(Q1, 0, 1, N, config, pt), 0],
              [make(Q1, 1, 0, N, config, pt), make(Q1, 1, 1, N, config, pt), 0],
              [0, 0, make(Q1, 2, 2, N, config, pt)]]) # balanced

Exx = (A[0][0]/(N*pt))*(1-(A[0][1]**2)/(A[0][0]*A[1][1]))
Eyy = (A[1][1]/(N*pt))*(1-(A[1][0]**2)/(A[0][0]*A[1][1]))
Gxy = A[2][2]/(N*pt)
vxy = A[1][0]/A[1][1]
vyx = A[0][1]/A[0][0]

# assume config then find Exx and Gxy

print(Exx, Gxy)
n = [Nxxc/(Exx*ec*pt), Nxyc/(Gxy*yc*pt)]
print(n)
Nxx = Exx*ec*N*pt
Nxy = Gxy*yc*N*pt
print(Nxx, Nxy)
print(N)
