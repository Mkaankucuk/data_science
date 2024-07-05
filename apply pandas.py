#apply
import pandas as pd
df = pd.DataFrame({
                   'degisken1':[10,23,33,22,11,99],
                   'degisken2':[100,253,333,262,111,969]},
                  columns=['degisken1','degisken2'])
df


#apply fonksiyonu dataframe in değişkenlerin üzerinde gezinme yeteneği olan
# aggegation yani toplulaştırma amacıyla kullanılan bir fonksiyondur

import numpy as np

df.apply(np.sum) 
# =============================================================================
# degisken1       198
# degisken2      2028
# =============================================================================

df.apply(np.mean)





import pandas as pd
df = pd.DataFrame({'gruplar':['a','b','c','a','b','c'],
                   'degisken1':[10,23,33,22,11,99],
                   'degisken2':[100,253,333,262,111,969]},
                  columns=['gruplar','degisken1','degisken2'])
df

df.groupby("gruplar").apply(np.sum)

# =============================================================================
#   gruplar  degisken1  degisken2
# gruplar                              
# a            aa         32        362
# b            bb         34        364
# c            cc        132       1302
# =============================================================================
