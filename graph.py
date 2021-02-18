from math import sin, cos
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def graph():
    x1 = np.linspace(-6, 6, 150)
    y1 = np.zeros(len(x1), dtype=float)
    for i in range(len(x1)):
        y1[i] = x1[i]*sin(x1[i]) + 3*cos(x1[i]) - x1[i]
    
    ax = plt.subplot(1, 1, 1)
    line1, = ax.plot(x1, y1, 'k-')
    
    plt.title('Graph')
    plt.xlabel('x', fontsize=18)
    plt.ylabel('y(x)', fontsize=18)
    plt.legend([line1],
               ['Legend',], fontsize=12,
               bbox_to_anchor=(1.1, 0.65), loc=2, borderaxespad=0.0)
    plt.grid()
    plt.show()

def squarewave():
    # Sampling rate 1000 hz / second
    t = np.linspace(0, 12, 1000, endpoint=True)
    
    # Plot the square wave signal
    plt.plot(t, signal.square(2*np.pi*(1/4)*t))
    
    plt.title('Square wave')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True, which='both')
    
    # Provide x axis and line color
    plt.axhline(y=0, color='k')
    # Set the max and min values for y axis
    plt.ylim(-2, 2)
    # Display the square wave drawn
    plt.show()

graph()
squarewave()

