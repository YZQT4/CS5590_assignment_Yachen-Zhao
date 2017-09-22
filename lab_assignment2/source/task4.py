import numpy as np
a=np.random.random_integers(0,80,(15,15))
max=a.max()
for i in range(0,15):
    for j in range(0,15):
        if a[i][j: j + 1]==max:
            a[i][j: j + 1]=100
print(a)