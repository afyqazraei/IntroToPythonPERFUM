import random
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

x=[0]
y=[0]
#z=[0]
steps=[0]

moves=[(0,1), (0,-1), (1,0), (-1,0)]
#dz=[-1,1]

for i in range (100000):
    dx, dy=random.choice(moves)
    #print(dx, dy)
    xs=x[i]+dx
    ys=y[i]+dy
    #zs=z[i]+random.choice(dz)
    x.append(xs)
    y.append(ys)
    #z.append(zs)
    
    st=steps[i]+1
    steps.append(st)
    
    
    #print(x)
    #print(y)
    #print(steps)
plt.plot(x,y)    
#ax.plot3D(x,y,z)
plt.show()
