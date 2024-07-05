#alt küme üzerinde işlme yapmak
import numpy as np
a= np.random.randint(10,size=(5,5))
a

alt_a = a[0:3,0:2]
alt_a

alt_a[0,0]=99999
alt_a[1,1]=888
alt_a

a

m= np.random.randint(10,size=(5,5))
m

alt_b = m[0:3,0:2].copy()# seçilen arrayi ana arrayden bağımsız yapar
alt_b
alt_b[0,0] = 999

m
