#birleştirme (join) işlemleri
import numpy as np
import pandas as pd
m = np.random.randint(1,30,size=(5,3))
df1 = pd.DataFrame(m,columns = ["var1","var2","var3"])
df1 

df2 = df1 + 99
df2

pd.concat([df1,df2])

# =============================================================================
#  var1  var2  var3
# 0    25     9    26
# 1    22    21    19
# 2    10    20    11
# 3    24    23    26
# 4    11    29    22
# 0   124   108   125
# 1   121   120   118
# 2   109   119   110
# 3   123   122   125
# 4   110   128   121
# =============================================================================

pd.concat([df1,df2],ignore_index=True) #indexin normalini yok say ignore

# =============================================================================
#   var1  var2  var3
# 0    25     9    26
# 1    22    21    19
# 2    10    20    11
# 3    24    23    26
# 4    11    29    22
# 5   124   108   125
# 6   121   120   118
# 7   109   119   110
# 8   123   122   125
# 9   110   128   121
# =============================================================================

df1.columns

df2.columns = ["var1","var2","deg3"]

df2
df1


pd.concat([df1,df2],join = "inner") #kesişimlerine göre  birleştirilicek

pd.concat([df1,df2],join_axes=[df1.columns]) #seçilmiş değişkenin değerline göre birleşim yapılır














