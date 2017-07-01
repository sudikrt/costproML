from numpy import *
from scipy import special, optimize
import matplotlib.pyplot as plt
a = arange (12)
a = a.reshape(3,2,2)
print a
f = lambda x: -special.jv(3, x)
sol = optimize.minimize(f, 1.0)
x = linspace(0, 10, 5000)
plt.plot (x, special.jv(3, x), '-', sol.x, -sol.fun, 'o')
plt.show()
plt.savefig('plot.png', dpi=96)
