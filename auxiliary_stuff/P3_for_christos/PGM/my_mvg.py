#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

# multivariate gaussian
# plus outlier

import matplotlib.pyplot as plt
import numpy as np
import math

np.random.seed(1) # repeatability

n=3000
x = np.random.normal(size=n)
y = np.random.normal(size=n)
# xp=[5.1, -8.1]
# yp=[-8.1, 5.1]
xp=[5.1]
yp=[-8.1 ]
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.plot(x,y,"b.",  xp, yp, "ro")
plt.grid()
plt.savefig("mvg.png")
plt.show()

