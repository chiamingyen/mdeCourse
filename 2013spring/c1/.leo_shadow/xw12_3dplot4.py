#@+leo-ver=4-thin
#@+node:mde.20130617220941.5842:@shadow c1/w12_3dplot4.py
#@@language python

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

try:
    import numpy as np
except:
    exit()

from deap import benchmarks

def h1_arg0(sol):
    return benchmarks.h1(sol)[0]

fig = plt.figure()
# ax = Axes3D(fig, azim = -29, elev = 50)
ax = Axes3D(fig)
X = np.arange(-25, 25, 0.5)
Y = np.arange(-25, 25, 0.5)
X, Y = np.meshgrid(X, Y)
Z = np.zeros(X.shape)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i,j] = h1_arg0((X[i,j],Y[i,j]))

ax.plot_surface(X, Y, Z, rstride=1, cstride=1,  norm=LogNorm(), cmap=cm.jet, linewidth=0.2)
 
plt.xlabel("x")
plt.ylabel("y")

plt.show()
#@nonl
#@-node:mde.20130617220941.5842:@shadow c1/w12_3dplot4.py
#@-leo
