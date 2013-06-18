
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt

try:
    import numpy as np
except:
    exit()

from deap import benchmarks

def griewank_arg0(sol):
    return benchmarks.griewank(sol)[0]

fig = plt.figure()
ax = Axes3D(fig, azim = -29, elev = 40)
# ax = Axes3D(fig)
X = np.arange(-50, 50, 0.5)
Y = np.arange(-50, 50, 0.5)
X, Y = np.meshgrid(X, Y)
Z = np.zeros(X.shape)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i,j] = griewank_arg0((X[i,j],Y[i,j]))

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0.2)
 
plt.xlabel("x")
plt.ylabel("y")

plt.show()
