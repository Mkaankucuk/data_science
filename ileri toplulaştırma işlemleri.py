# ileri toplulaştırma işlemleri 
#aggregate

import pandas as pd
df = pd.DataFrame({'gruplar':['a','b','c','a','b','c'],
                   'degisken1':[10,23,33,22,11,99],
                   'degisken2':[100,253,333,262,111,969]},
                  columns=['gruplar','degisken1','degisken2'])
df

df.groupby("gruplar").mean()

import numpy as np

df.groupby("gruplar").aggregate(["min",np.median,max])
# grouby ile veri setini gruplara göre böl 
# ne describe gibi hepisini ne de tek tek 
# aggregate ile liste formunda beklediği fonksiyonları bize getiriyor

# pandas ın içindeki fonksiyonları aggregate edersek tırnaklı veya tırnaksız kullanabiliriz
# burada butun degıskenlere uygulayacak

df.groupby("gruplar").aggregate({"degisken1":"min","degisken2":"max"})

# =============================================================================
# degisken1  degisken2
# gruplar                      
# a               10        262
# b               11        253
# c               33        969
# =============================================================================
