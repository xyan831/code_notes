# graph
# xyan831

from math import sin, cos

import numpy as np
import matplotlib.pyplot as plt

from scipy import signal
from pylab import pi, logspace, polymul

def graph():
	# set up arrays
	x1 = np.linspace(-6, 6, 150)
	y1 = np.zeros(len(x1), dtype=float)
	y2 = np.zeros(len(x1), dtype=float)
	y3 = np.zeros(len(x1), dtype=float)
	y4 = np.zeros(len(x1), dtype=float)
	# set up equations
	for i in range(len(x1)):
		y1[i] = abs(x1[i])
		y2[i] = x1[i]**2
		y3[i] = sin(x1[i])
		y4[i] = cos(x1[i])
	# plot equations
	ax = plt.subplot(1, 1, 1)
	line1, = ax.plot(x1, y1, 'k-')
	line2, = ax.plot(x1, y2, 'r:')
	line3, = ax.plot(x1, y3, 'b--')
	line4, = ax.plot(x1, y4, 'g-.')
	# vertical line
	plt.axvline(x=0, color='y')
	# set axis limits
	plt.xlim([-7, 7])
	plt.ylim([-3, 3])
	# label title and axis
	plt.title('Graph')
	plt.xlabel('x', fontsize=18)
	plt.ylabel('y(x)', fontsize=18)
	plt.legend([line1, line2, line3, line4],
			['y1', 'y2', 'y3', 'y4'], fontsize=12,
			bbox_to_anchor=(1.02, 0.65), loc=2, borderaxespad=0.0)
	# add grid and show plot
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

def bodeplot():
	# denominator and numerator
	denominator = polymul([1, 0], [1, 16, 100])
	numerator = [7.5]
	numerator = polymul(numerator, [0.2, 1])
	numerator = polymul(numerator, [1, 1])
	
	system = signal.lti(numerator, denominator)
	domain = logspace(-3, 3)
	omega, magnitude, phase = signal.bode(system, 2*pi*domain)
	# break frequencies
	break_frequencies = [1, 5, 10]
	
	_, plot = plt.subplots(2, sharex=True)
	plot[0].semilogx(omega, magnitude)
	plot[0].vlines(break_frequencies, ymin=min(magnitude), ymax=max(magnitude), colors='C1')
	plot[0].set_title('Bode Plot')
	plot[1].semilogx(omega, phase)
	plot[1].vlines(break_frequencies, ymin=min(magnitude), ymax=max(magnitude), colors='C1')

graph()
#squarewave()
#bodeplot()
