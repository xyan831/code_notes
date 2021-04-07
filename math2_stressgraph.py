# MEEN 489-507 In Class Work
# Xiaochen Yan UIN: 327002462
# 4/6/2021

from math import radians, sin, cos
import matplotlib.pyplot as plt
import numpy as np

# normal and shear stress values
sx = 100
sy = -50
txy = 30

# theta from 0-180 degrees
theta = np.linspace(0, 180, 181)
th = np.zeros(len(theta), dtype=float)
nsx = np.zeros(len(theta), dtype=float)
nsy = np.zeros(len(theta), dtype=float)
ntxy = np.zeros(len(theta), dtype=float)

# equations
for i in range(len(theta)):
    th[i] = radians(theta[i])
    nsx[i] = ((sx+sy)/2) + (((sx-sy)/2)*cos(2*th[i])) + (txy*sin(2*th[i]))
    nsy[i] = ((sx+sy)/2) - (((sx-sy)/2)*cos(2*th[i])) - (txy*sin(2*th[i]))
    ntxy[i] = -(((sx-sy)/2)*sin(2*th[i])) + (txy*cos(2*th[i]))

# graph
ax = plt.subplot(1, 1, 1)
line1, = ax.plot(theta, nsy, 'r-')
line2, = ax.plot(theta, nsx, 'b-')
line3, = ax.plot(theta, ntxy, 'k-')

# axis titles and legend
plt.title('MEEN 489-507 In Class Work 4/6/2021')
plt.xlabel('Degrees', fontsize=18)
plt.ylabel('Stress [MPa]', fontsize=18)
plt.legend([line1, line2, line3],
           ['Sx', 'Sy', 'Txy'], fontsize=12,
           bbox_to_anchor=(1.1, 0.65), loc=2, borderaxespad=0.0)
plt.grid()
plt.show()
