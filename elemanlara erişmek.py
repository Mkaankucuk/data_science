#ındex ile elemanlara erişmek
import numpy as np
a = np.random.randint(10,size= 10)
a
a[-1]

a[0]=100
a
m = np.random.randint(10,size=(3,5))
m
m[0,0] #ilk satır sonra sütun 
m[1,1]

m[1,4]=2.2
