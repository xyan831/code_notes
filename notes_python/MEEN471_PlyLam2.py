from math import sqrt, radians, sin, cos
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
# laminate config
c = [0]*4 + [45] + [0]*3 + [-45, 90]
config = c + list(reversed(c))
N = len(config)
pt = 0.005
ply = 1
z = pt*(ply-0.5 - N/2)
Nxx = 1000  # normal stress resultant
Nyy = 0
Nxy = 0     # shear stress resultant 
Mxx = 10     # bending stress resultant
Myy = 0
Mxy = 0     # twisting stress resultant
# strengths
Slt = 217.5*K
Slc = 217.5*K
Stt = 5.80*K
Stc = 35.7*K
Slts = 9.86*K

# matrix solve linear equation
def mat_lin(na, nb):
    lin_eq = np.linalg.solve(na, nb)
    return lin_eq
# matrix
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
def S1(E11, E22, G12, v12, v21): # local strain to stress
    S1 = np.array([[1/E11, -v12/E11, 0],
                   [-v21/E22, 1/E22, 0],
                   [0, 0, 1/G12]])
    return S1
def Q2(Q1, T1, T2): # global stress to strain
    return np.linalg.inv(T1) @ Q1 @ T2
def S2(Q2): # global strain to stress
    return np.linalg.inv(Q2)

def make(Q1, x, y, N, config, pt, let):
    a = 0
    b = 0
    d = 0
    for i in range(1, N+1):
        Q = Q2(Q1, T1(radians(config[i-1])), T2(radians(config[i-1])))
        zk = pt*(i - N/2)
        zk1 = pt*(i-1 - N/2)
        a += Q[x][y]*(zk-zk1)
        b += (1/2)*Q[x][y]*(zk**2-zk1**2)
        d += (1/3)*Q[x][y]*(zk**3-zk1**3)
    if let=='A':
        return a
    elif let=='B':
        return b
    elif let=='D':
        return d

# matrix
Q1 = Q1(E11, E22, G12, v12, v21)

def matA(Q1, N, bal):
    A = np.array([[make(Q1, 0, 0, N, config, pt, 'A'), make(Q1, 0, 1, N, config, pt, 'A'), make(Q1, 0, 2, N, config, pt, 'A')],
                  [make(Q1, 1, 0, N, config, pt, 'A'), make(Q1, 1, 1, N, config, pt, 'A'), make(Q1, 1, 2, N, config, pt, 'A')],
                  [make(Q1, 2, 0, N, config, pt, 'A'), make(Q1, 2, 1, N, config, pt, 'A'), make(Q1, 2, 2, N, config, pt, 'A')]])
    A_b = np.array([[make(Q1, 0, 0, N, config, pt, 'A'), make(Q1, 0, 1, N, config, pt, 'A'), 0],
                    [make(Q1, 1, 0, N, config, pt, 'A'), make(Q1, 1, 1, N, config, pt, 'A'), 0],
                    [0, 0, make(Q1, 2, 2, N, config, pt, 'A')]]) # balanced
    if bal == True:
        return A_b
    else:
        return A

def matB(Q1, N, sym):
    B = np.array([[make(Q1, 0, 0, N, config, pt, 'B'), make(Q1, 0, 1, N, config, pt, 'B'), make(Q1, 0, 2, N, config, pt, 'B')],
                  [make(Q1, 1, 0, N, config, pt, 'B'), make(Q1, 1, 1, N, config, pt, 'B'), make(Q1, 1, 2, N, config, pt, 'B')],
                  [make(Q1, 2, 0, N, config, pt, 'B'), make(Q1, 2, 1, N, config, pt, 'B'), make(Q1, 2, 2, N, config, pt, 'B')]])
    B_s = np.array([[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]) # symmetric
    if sym == True:
        return B_s
    else:
        return B

A = matA(Q1, N, True)
B = matB(Q1, N, True)

D = np.array([[make(Q1, 0, 0, N, config, pt, 'D'), make(Q1, 0, 1, N, config, pt, 'D'), make(Q1, 0, 2, N, config, pt, 'D')],
              [make(Q1, 1, 0, N, config, pt, 'D'), make(Q1, 1, 1, N, config, pt, 'D'), make(Q1, 1, 2, N, config, pt, 'D')],
              [make(Q1, 2, 0, N, config, pt, 'D'), make(Q1, 2, 1, N, config, pt, 'D'), make(Q1, 2, 2, N, config, pt, 'D')]])

matrix = np.array([[A[0][0], A[0][1], A[0][2], B[0][0], B[0][1], B[0][2]],
                   [A[1][0], A[1][1], A[1][2], B[1][0], B[1][1], B[1][2]],
                   [A[2][0], A[2][1], A[2][2], B[2][0], B[2][1], B[2][2]],
                   [B[0][0], B[0][1], B[0][2], D[0][0], D[0][1], D[0][2]],
                   [B[1][0], B[1][1], B[1][2], D[1][0], D[1][1], D[1][2]],
                   [B[2][0], B[2][1], B[2][2], D[2][0], D[2][1], D[2][2]]])

# maximum stress failure
#maxstress_R = [Slt/s11, Stt/s22, Slts/t12] # pick lowest R

# tsai-wu failure
def tswu(Slt, Slc, Stt, Stc, Slts, s11, s22, t12):
    F11 = 1/(Slt*Slc)
    F22 = 1/(Stt*Stc)
    F12 = (-1/2)*sqrt(F11*F22)
    F66 = 1/(Slts**2)
    F1 = (1/Slt) - (1/Slc)
    F2 = (1/Stt) - (1/Stc)
    # r2*R^2 + r1*R - 1 = 0
    r2 = F11*(s11**2) + 2*F12*s11*s22 + F22*(s22**2) + F66*(t12**2)
    r1 = F1*s11 + F2*s22
    if (r1**2 - 4*r2*(-1))>=0:
        return [(-r1+sqrt(r1**2-4*r2*(-1)))/(2*r2), (-r1-sqrt(r1**2-4*r2*(-1)))/(2*r2)]
    else:
        return 0

# laminate
lam = mat_lin(matrix, np.array([Nxx, Nyy, Nxy, Mxx, Myy, Mxy]))
midstrain = np.array([lam[0], lam[1], lam[2]]) # laminate mid-plane strain
curvature = np.array([lam[3], lam[4], lam[5]]) # laminate curvature

# specific ply
plystrain = midstrain + z*curvature                        # global strain
for ply in range(1, N):
    locstrain = mat_lin(T2(radians(config[ply-1])), plystrain) # local strain
    locstress = mat_lin(np.linalg.inv(Q1), locstrain)          # local stress
    s11 = locstress[0]
    s22 = locstress[1]
    t12 = locstress[2]
    print('Ply: ', ply)
    print(tswu(Slt, Slc, Stt, Stc, Slts, s11, s22, t12))

# calculator
#print('midstrain: ', midstrain)
#print('curvature', curvature)
#print('global strain', plystrain)
#print(Nxx*1.0875, Mxx*1.0875)
