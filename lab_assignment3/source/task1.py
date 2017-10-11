import numpy as np
import matplotlib.pyplot as plt

#sleeping time according to average age
a=np.array([[1,2,6,10,16,23,28,35,50,60,70],[16,14,12,10,8,7,7,7,6,6,5]])
sumx=0
sumy=0
for i in range(0,11):
    sumx=sumx+a[0][i:i+1]
xavg=sumx/10
for j in range(0,11):
    sumy=sumy+a[1][j:j+1]
yavg=sumy/11
sumup=0
sumd=0
for i in range(0,11):
    sumup=sumup+(a[0][i:i+1]-xavg)*(a[1][i:i+1]-yavg)
for i in range(0,11):
    sumd=sumd+(a[0][i:i+1]-xavg)*(a[0][i:i+1]-xavg)
B1=sumup/sumd
B2=yavg-B1*xavg
x = np. linspace (4 , 10, 1000)
y=B1*x+B2
plt.plot (x , y)
plt.show()
print(B1,B2)
