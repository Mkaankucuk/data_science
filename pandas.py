#pandas
# panel data
# ekonometrik ve finansal calısmalar ıcın dogmustur
# veri manuplasyonu ve verı analızı ıcın

# pandas serisi olusturmak

import pandas as pd

pd.Series([10,88,3,4,5]) 
# =============================================================================
# 0    10
# 1    88
# 2     3
# 3     4
# 4     5
# 
# =============================================================================

seri = pd.Series([10,88,3,4,5]) 
type(seri)

seri.axes # serinin indexlerini söyler 0 dan 5 e kadar

seri.dtype # serinin ıcındekı degerlerle alakalı bılgılerı almak ıcın kullanılır

seri.size # serinin eleman sayısı

seri.ndim # serinin boyutu 

seri.values #array([10, 88,  3,  4,  5], dtype=int64)

seri.head() # kaç yazarsan baştan o kadar eleman getirir

#index isimlendirmesi 
pd.Series([99,22,332,94,5], index = [1,3,5,7,9])

pd.Series([99,22,332,94,5], index = ["a","b","c","d","e"])

seri = pd.Series([99,22,332,94,5], index = ["a","b","c","d","e"])
seri["a"] #99

seri["a":"c"] 
# =============================================================================
# a     99
# b     22
# c    332
# =============================================================================

# sozluk uzerınden lıste olusturmak 
sozluk = {"reg":10,"log":11,"cart":12}
seri = pd.Series(sozluk)
seri
# =============================================================================
# reg     10
# log     11
# cart    12
# 
# =============================================================================


# iki seriyi birlestirerek seri olusturma
pd.concat([seri,seri])
# =============================================================================
# 
# reg     10
# log     11
# cart    12
# reg     10
# log     11
# cart    12
# 
# =============================================================================
