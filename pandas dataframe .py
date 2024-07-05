# Pandas DataFrame oluşturma
import pandas as pd

l = [1,2,39,67,90]

#ilk argüman hangi veriyi kullanıcaksın , isimlendirmek ister misin

pd.DataFrame(l,columns= ["değişken_ismi"])

import numpy as np

m = np.arange(1,10).reshape((3,3))
m

pd.DataFrame(m,columns=("var1","var2","var3"))

# columns sutun

# df isimlendirme
df= pd.DataFrame(m,columns=("var1","var2","var3"))
df.head()

df.columns = ("deg1","deg2","deg3") # columns u değiştiriyor
df
type(df)

df.axes #satır ve sutun bilgilei
df.ndim
df.size
df.value # bu numpy.ndarray formatına çevirip gösterşyor değişknelri
df.head()
df.tail()

