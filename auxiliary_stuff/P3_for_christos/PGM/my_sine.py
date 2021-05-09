#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import math
# import random

l=50
period=5
x = np.arange(0,l,0.01)
y =  [ math.sin(2* math.pi * t/period) for t in x]
np.random.seed(1) # repeatability
xp = np.random.uniform(0,l,30)
yp =  [ math.sin(2* math.pi * t/period) for t in xp]
xpp=period/4.0
ypp=  - math.sin(2*math.pi * xpp/period)
fig, axs = plt.subplots(2,2)
# plt.xlabel("x")
# plt.ylabel("y")
ax=axs[0,0]
ax.plot(x,y,"g--", xp,yp,"bo", [xpp], [ypp], "ro")

ax=axs[1,1]
ax.plot(xp,yp,"bo", [xpp], [ypp], "bo")
plt.savefig("my-sine.png")
plt.show()

plt.clf()
plt.plot(x,y,"g--", xp,yp,"bo", [xpp], [ypp], "ro")
plt.savefig("sine-all.png")
plt.show()

plt.clf()
plt.plot([xpp], [ypp], "bo")
plt.savefig("sine-init.png")
plt.show()

plt.clf()
plt.plot(x,y,"g-")
plt.savefig("sine-only.png")
plt.show()
