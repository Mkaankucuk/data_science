# pandas eleman işlemleri

import pandas as pd

a = pd.Series([1,2,33,444,75])
seri = pd.Series(a) 
seri[0]

seri[0:3]

seri = pd.Series([121,200,150,99],index = ["reg","loj","cart","rf"])
seri

seri.index

# =============================================================================
# Index(['reg', 'loj', 'cart', 'rf'], dtype='object')
# =============================================================================

seri.keys
# =============================================================================
# 
# loj     200
# cart    150
# rf       99
# =============================================================================
list(seri.items()) #liste içerisnden keylerin karşılık geldiği değerleri gösterir 

#eleman sorgulama 
"reg" in seri # yazdığımız eleman içinde mi  True

#fancy eleman
seri[["rf","reg"]] #rf      99
                    #reg    121


seri["reg"]=130 #elemanı değiştirdi
seri["reg"]



