# DataFrame eleman işlemleri

import numpy as np
s1= np.random.randint(10,size=5)
s2= np.random.randint(10,size=5)
s3= np.random.randint(10,size=5)


sozluk = {"var1":s1,"var2":s2,"var3":s3}
sozluk

import pandas as pd 

df=pd.DataFrame(sozluk)
df

# =============================================================================
# var1  var2  var3
# 0     9     3     7
# 1     4     9     2
# 2     0     6     9
# 3     5     7     2
# 4     7     6     9
# =============================================================================

df[0:1]

df.index = ["a","b","c","d","e"]
df

df["c":"e"]

# =============================================================================
# var1  var2  var3
# c     0     6     9
# d     5     7     2
# e     7     6     9
# 
# =============================================================================

# silme 
df.drop("a",axis=0) # veri yapısından kalıcı silinmedi

# =============================================================================
#  var1  var2  var3
# b     4     9     2
# c     0     6     9
# d     5     7     2
# e     7     6     9
# 
# =============================================================================

#inplace görevi dataframe de kalıcı olmak

df.drop("a",axis = 0 , inplace = True)
df

#fancy

l=["c","e"]
df.drop(l,axis=0)

# =============================================================================
#  var1  var2  var3
# b     4     9     2
#  d     5     7     2
# =============================================================================

# değişkenler icin

df

"var1" in df
l = ["var1","var4","var2"]

for i in l:
    print(i in df )

df
df["var4"] = df["var1"]/df["var2"]
df

# =============================================================================
#    var1  var2  var3      var4
# b     4     9     2  0.444444
# c     0     6     9  0.000000
# d     5     7     2  0.714286
# e     7     6     9  1.166667
# 
# 
# 
# =============================================================================

# degisken silmek 
df.drop("var4",axis=1)

df

#fancy ile silme

l = ["var1","var2"]

df.drop(l,axis=1)












