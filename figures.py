#!/usr/bin/env python
"""
Illustrate simple contour plotting, contours on an image with
a colorbar for the contours, and labelled contours.

See also contour_image.py.
"""
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from pylab import *

# Steepest Descent example


delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.5, 2.5, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z = Z1

plt.figure()
U, V = np.gradient(Z)
CS = plt.contour(X, Y, Z)
plt.arrow(-1.44,-1.44,1.43,1.43)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Steepest Descent in a nice situation')
plt.savefig('Figures/steepestDescentNice.eps', format='eps', dpi=1000)
plt.show()

Z = 0.1*(0.3*(X-3)**2 + Y**2 + X*Y)

x = np.arange(-0.5, 0.5, delta)
y = np.arange(0, 1, delta)
X, Y = np.meshgrid(x, y)
Z = sin(0.5 * X**2 - 0.25 * Y**2 + 3) * cos(2*X + 1 - exp(Y))
plt.figure()
U, V = np.gradient(Z)
CS = plt.contour(X, Y, Z,32)
plt.arrow(-0.25,0.32,0.32,-0.03, length_includes_head = True, fc="k", ec="k",
head_width=0.01, head_length=0.01)
plt.arrow(0.07,0.29,0.04,0.33, length_includes_head = True , fc="k", ec="k",
head_width=0.01, head_length=0.01)
plt.arrow(0.11,0.62,0.09,-0.01, length_includes_head = True, fc="k", ec="k",
head_width=0.01, head_length=0.01)
plt.arrow(0.2,0.61,0.02,0.11, length_includes_head = True, fc="k", ec="k",
head_width=0.01, head_length=0.01)
plt.arrow(0.22,0.72,0.04,-0.01, length_includes_head = True, fc="k", ec="k",
head_width=0.01, head_length=0.01)
plt.arrow(0.26,0.71,0.01,0.06, length_includes_head = True, fc="k", ec="k",
head_width=0.01, head_length=0.01)
plt.arrow(0.27,0.77,0.04,-0.005, length_includes_head = True, fc="k", ec="k",
head_width=0.01, head_length=0.01)
plt.arrow(0.31,0.765,0.005,0.02, length_includes_head = True, fc="k", ec="k",
head_width=0.01, head_length=0.01)
plt.arrow(0.315,0.785,0.015,-0.005, length_includes_head = True, fc="k", ec="k",
head_width=0.01, head_length=0.01)
plt.arrow(0.33,0.78,0.005,0.015, length_includes_head = True, fc="k", ec="k",
head_width=0.01, head_length=0.01)
plt.arrow(0.335,0.795,0.005,-0.005, length_includes_head = True, fc="k", ec="k",
head_width=0.01, head_length=0.01)
plt.arrow(0.34,0.79,0.005,0.02, length_includes_head = True, fc="k", ec="k",
head_width=0.01, head_length=0.01)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Steepest Descent in a bad situation: f(x, y) = 0.1(0.3*(x-3)^2 + y^2 + xy)')
plt.show()

# Internet examples

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
# difference of Gaussians
Z = 10.0 * (Z2 - Z1)



# Create a simple contour plot with labels using default colors.  The
# inline argument to clabel will control whether the labels are draw
# over the line segments of the contour, removing the lines beneath
# the label
plt.figure()
U, V = np.gradient(Z)
CS = plt.contour(X, Y, Z)
plt.arrow(-1,-1,1,1)
#Q = plt.quiver( X, Y, U, V)
#qk = quiverkey(Q, 0.9, 0.95, 2, '',
#               labelpos='E',
#               coordinates='figure',
#               fontproperties={'weight': 'bold'})
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Simplest default with labels')
plt.show()

# contour labels can be placed manually by providing list of positions
# (in data coordinate). See ginput_manual_clabel.py for interactive
# placement.
plt.figure()
CS = plt.contour(X, Y, Z)
manual_locations = [(-1, -1.4), (-0.62, -0.7), (-2, 0.5), (1.7, 1.2), (2.0, 1.4), (2.4, 1.7)]
plt.clabel(CS, inline=1, fontsize=10, manual=manual_locations)
plt.title('labels at selected locations')


# You can force all the contours to be the same color.
plt.figure()
CS = plt.contour(X, Y, Z, 6,
                 colors='k', # negative contours will be dashed by default
                 )
plt.clabel(CS, fontsize=9, inline=1)
plt.title('Single color - negative contours dashed')

# You can set negative contours to be solid instead of dashed:
matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
plt.figure()
CS = plt.contour(X, Y, Z, 6,
                 colors='k', # negative contours will be dashed by default
                 )
plt.clabel(CS, fontsize=9, inline=1)
plt.title('Single color - negative contours solid')


# And you can manually specify the colors of the contour
plt.figure()
CS = plt.contour(X, Y, Z, 6,
                 linewidths=np.arange(.5, 4, .5),
                 colors=('r', 'green', 'blue', (1,1,0), '#afeeee', '0.5')
                 )
plt.clabel(CS, fontsize=9, inline=1)
plt.title('Crazy lines')


# Or you can use a colormap to specify the colors; the default
# colormap will be used for the contour lines
plt.figure()
im = plt.imshow(Z, interpolation='bilinear', origin='lower',
                cmap=cm.gray, extent=(-3,3,-2,2))
levels = np.arange(-1.2, 1.6, 0.2)
CS = plt.contour(Z, levels,
                 origin='lower',
                 linewidths=2,
                 extent=(-3,3,-2,2))

#Thicken the zero contour.
zc = CS.collections[6]
plt.setp(zc, linewidth=4)

plt.clabel(CS, levels[1::2],  # label every second level
           inline=1,
           fmt='%1.1f',
           fontsize=14)

# make a colorbar for the contour lines
CB = plt.colorbar(CS, shrink=0.8, extend='both')

plt.title('Lines with colorbar')
#plt.hot()  # Now change the colormap for the contour lines and colorbar
plt.flag()

# We can still add a colorbar for the image, too.
CBI = plt.colorbar(im, orientation='horizontal', shrink=0.8)

# This makes the original colorbar look a bit out of place,
# so let's improve its position.

l,b,w,h = plt.gca().get_position().bounds
ll,bb,ww,hh = CB.ax.get_position().bounds
CB.ax.set_position([ll, b+0.1*h, ww, h*0.8])


plt.show()


# example of steepest descent

# From calculation, we expect that the local minimum occurs at x=9/4
 
x_old = 0
x_new = -0.28 # The algorithm starts at x=6
y_old = 0
y_new = 0.315
eps = 1.0 # step size
precision = 0.00001
 

Z = sin(0.5 * X**2 - 0.25 * Y**2 + 3) * cos(2*X + 1 - exp(Y))

def x_prime(X, Y):
    return X * cos(0.5 * X**2 - 0.25 * Y**2 + 3) * cos(2*X + 1 - exp(Y)) - 2 * sin(0.5 * X**2 - 0.25 * Y**2 + 3) * sin(2* X + 1 - exp(Y))

def y_prime(X, Y):
    return -0.5 * Y * cos(0.5 * X**2 - 0.25 * Y**2 + 3) * cos(2*X + 1 - exp(Y)) + exp(Y) * sin(0.5 * X**2 - 0.25 * Y**2 + 3) * sin(2* X + 1 - exp(Y))
 

while abs(x_new - x_old) > precision:
      x_old = x_new
      y_old = y_new
      x_new = x_old - eps * x_prime(x_old, y_old)
      y_new = y_old - eps * y_prime(x_old, y_old)
      print(x_new, y_new)

while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new = x_old - eps * f_prime(x_old)
    print "new step", x_new
print "Local minimum occurs at ", x_new
