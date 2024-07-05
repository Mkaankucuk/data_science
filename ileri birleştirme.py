#ileri birleştirme

import pandas as pd 

df1= pd.DataFrame({'calısanlar':['ali','veli','ayse','fatma'],
                  'grup':['muhasebe','muhendislik','muhendıslık',"ik"] })
df1

df2 = pd.DataFrame({'calısanlar':['ayse','ali','veli','fatma'],
                  'ilk_giris':[2010,2009,2014,2019] })
df2

pd.merge(df1,df2) # burada calısanlara göre birlestirdi

# =============================================================================
# calısanlar         grup  ilk_giris
# 0        ali     muhasebe       2009
# 1       veli  muhendislik       2014
# 2       ayse  muhendıslık       2010
# 3      fatma           ik       2019
# =============================================================================

pd.merge(df1,df2,on = "calısanlar") #calısanlar üstünde birleştir

# coktan teke
df3 = pd.merge(df1,df2)
df3

df4 = pd.DataFrame({'grup':['muhasebe','muhendıslık','ik'],
               'mudur':['caner','mustafa','berkcan']})

df4

pd.merge(df3,df4) #gruptaki değerleri birleştirdi

# =============================================================================
#  calısanlar         grup  ilk_giris    mudur
# 0        ali     muhasebe       2009    caner
# 1       ayse  muhendıslık       2010  mustafa
# 2      fatma           ik       2019  berkcan
# =============================================================================

# coktan coka
df5 = pd.DataFrame({'grup':['muhasebe','muhasebe',
                           'muhensıklık ','muhendislik','ik','ik'],
                   'yetenekler':['matematik','excel','kodlama','linux',
                                 'excel','yonetim']})

df5


pd.merge(df1,df5) #mesela isimleri çokladı



# =============================================================================
# calısanlar         grup yetenekler
# 0        ali     muhasebe  matematik
# 1        ali     muhasebe      excel
# 2       veli  muhendislik      linux
# 3      fatma           ik      excel
# 4      fatma           ik    yonetim
# 
# 
# 
# =============================================================================



