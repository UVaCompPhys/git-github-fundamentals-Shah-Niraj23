import math as m
import matplotlib.pyplot as plt
import numpy as np

for n in np.arange(51):
        R = []
        V = []
        for r in np.arange(1,2.05,0.05):
                R.append(r)
                v = (pow(m.pi, n/2) * pow(r, n))/(m.gamma(n/2 + 1))
                V.append(v)
        plt.plot(R,V)
plt.xlabel("Radius (R)")
plt.ylabel("Volume(V)")
plt.title("Volume of n-dimensional Sphere as a function of n and R")

plt.show()
plt.savefig('Sphere.pdf')
