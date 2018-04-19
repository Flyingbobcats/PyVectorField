from vectorField import vectorField
import numpy as np
from matplotlib import pyplot as plt
from dubinsUAV import dubinsUAV


saveField = False
saveUAVPath = False

uav = dubinsUAV()

velocity = 0.25
gamma = 1.0




vf = vectorField()


vf.setupObst(0,0,gamma)
vf.obstH = 6.1

plt.ion()

vf.simulateDubins()


plt.show()

plt.pause(10000)
plt.savefig('flight.pdf')


if saveField:
    np.savetxt('Xs', X, fmt='%5e', delimiter=',')
    np.savetxt('Ys', Y, fmt='%5e', delimiter=',')
    np.savetxt('Us', U, fmt='%5e', delimiter=',')
    np.savetxt('Vs', V, fmt='%5e', delimiter=',')

if saveUAVPath:

    np.savetxt('UAVpathx',uav.xs,delimiter=',')
    np.savetxt('UAVpathy', uav.ys, delimiter=',')
