import random
import matplotlib.pyplot as plt

x=[0]
steps=[0]

moves=[-1,1]

for i in range (10000):
    xs=x[i]+random.choice(moves)
    x.append(xs)
    
    st=steps[i]+1
    steps.append(st)
    
    
    #print(x)
    #print(steps)
    
plt.plot(x, steps)
plt.show()