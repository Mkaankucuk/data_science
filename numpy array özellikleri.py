#numpy array özellikleri

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam elaman sayısı
# dtype:array veri tipi

import numpy as np

np.random.randint(10,size = 10)

a = np.random.randint(10,size = 10)
a.ndim  # tek boyutlu bir array
a.shape #  tek boyutlu olduğu için 1 boyunun eleman bilgisi var
a.size #  toplam eleman sayısı verdi

a.dtype # boyutunu verir

b = np.random.randint(10,size=(3,5))
b
b.ndim
b.shape
b.size
b.dtype
