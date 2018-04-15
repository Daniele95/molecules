import numpy as np
import sdeint

k = 1.
g = 1.

x0 = 1.
v0 = 1.

A = np.array([[ 0., 1. ],
              [ -k, -g ]])

B = np.diag([0., 1.])

t = np.linspace(0.0, 10.0, 10001)
X0 = np.array([x0, v0])

def F(x, t):
    return A.dot(x)

def G(x, t):
    return B

X = sdeint.itoint(F, G, X0, t)

#plot( t, X[0] )