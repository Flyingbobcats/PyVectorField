from vectorField import vectorField
import numpy as np
from matplotlib import pyplot as plt
from UAV import UAV


saveField = False
saveUAVPath = False

uav = UAV()

velocity = 25
gamma = 3.8013
obstR = uav.v / 0.35+200
x_start = -(velocity/0.35*gamma+obstR)*1.1
uav.setup(x_start, 0, velocity, 0, 0.1)

vf = vectorField()


vf.setupObst(uav,200,-200,0,gamma)
vf.obstH = 4.222

xs = np.linspace(-400,400,2*50/4)
ys = xs
X,Y = np.meshgrid(xs,ys)

# U = np.nan((len(xs),len(xs)))
# V = np.nan((len(xs),len(xs)))

U = np.empty((len(xs),len(xs)))
U[:] = np.nan

V = np.empty((len(xs),len(xs)))
V[:] = np.nan




# for i in range(0, len(xs)):
#     for j in range(0, len(ys)):
#         # Vg = vf.calcPath(xs[i],ys[j])
#
#         Vg = vf.calcObst(xs[i], ys[j])
#
#         Vg = vf.getVFatXY(xs[i], ys[j])
#
#
#
#         U[i][j] = Vg[0][0]
#         V[i][j] = Vg[1][0]
#         X[i][j] = xs[i]
#         Y[i][j] = ys[j]
#
#
# plt.quiver(X,Y,U,V,scale=25)
# plt.plot([-50,50],[0,0])
# # plt.show()


plt.ion()
while uav.x < -1*x_start:

    plt.cla()
    if abs(uav.x)<obstR:
        for i in range(0, len(xs)):
            for j in range(0, len(ys)):


                Vg = vf.getVFatXY(xs[i], ys[j])



                U[i][j] = Vg[0][0]
                V[i][j] = Vg[1][0]
                X[i][j] = xs[i]
                Y[i][j] = ys[j]


        plt.quiver(X,Y,U,V,scale=50)

    Vg = vf.getOptVF(uav)
    heading = np.arctan2(Vg[1], Vg[0])
    uav.update_pos(heading)
    vf.pltObstacle()
    plt.plot(uav.xs, uav.ys, 'r')
    plt.quiver(uav.x,uav.y,uav.vx,uav.vy,color='b')
    plt.quiver(uav.x,uav.y,Vg[0],Vg[1],color='r')

    plt.axis('equal')


    plt.pause(0.01)


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
