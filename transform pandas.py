#transform
import pandas as pd
df = pd.DataFrame({'gruplar':['a','b','c','a','b','c'],
                   'degisken1':[10,23,33,22,11,99],
                   'degisken2':[100,253,333,262,111,969]},
                  columns=['gruplar','degisken1','degisken2'])
df

# hatırlatma lambda fonksiyon isimlendirmesi yapmadan fonksiyon tanımlıyorduk


df_a = df.iloc[:,1:3] # slice dataframe de iloc ya da loc ile yapılır

df_a.transform(lambda x: x-x.mean())
# =============================================================================
# 
# degisken1  degisken2
# 0      -23.0     -238.0
# 1      -10.0      -85.0
# 2        0.0       -5.0
# 3      -11.0      -76.0
# 4      -22.0     -227.0
# 5       66.0      631.0
# =============================================================================

df_a.transform(lambda x: (x-x.mean())/x.std())
