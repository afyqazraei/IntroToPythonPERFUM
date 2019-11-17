import random
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")


x=[0]
y=[0]
z=[0]
steps=[0]

moves=[(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]

for i in range (100000):
    dx, dy, dz=random.choice(moves)
    xs=x[i]+dx
    ys=y[i]+dy
    zs=z[i]+dz
    x.append(xs)
    y.append(ys)
    z.append(zs)
    
    st=steps[i]+1
    steps.append(st)
    
    
    #print(x)
    #print(y)
    #print(steps)
    
ax.plot3D(x,y,z)
plt.show()
