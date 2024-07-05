# filter 


import pandas as pd
df = pd.DataFrame({'gruplar':['a','b','c','a','b','c'],
                   'degisken1':[10,23,33,22,11,99],
                   'degisken2':[100,253,333,262,111,969]},
                  columns=['gruplar','degisken1','degisken2'])
df

def filter_func(x):
    return x["degisken1"].std()>9

df.groupby("gruplar").filter(filter_func)

# =============================================================================
# gruplar  degisken1  degisken2
# 2       c         33        333
# 5       c         99        969
# =============================================================================
