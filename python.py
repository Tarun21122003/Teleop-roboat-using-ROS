import numpy as np
import matplotlib.pyplot as plt
y=[]
for i in range(1000000):
    mylist=[1,2,3,4,5,6]
    x = np.random.choice(mylist)
    y.append(x)

z={}
for item in y:
    if item in z:
        z[item]+=1
    else:
        z[item]=1

print(z)
##    
##plt.plot(z)
##plt.show
