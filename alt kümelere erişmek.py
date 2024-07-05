#slicing ile elemanlara erişmek(array alt kümesine erişmek)
import numpy as np
a = np.arange(20,30)
a
a[0:3] # 0 dan 3e kadar kes işlemi slice



a[1::2] # ilk  elemandan başla 2şer 2 şer art
a[0::3]

#iki boyutlu slice işlemleri
m = np.random.randint(10,size =(5,5))
m

m[:,0] # : ile bütün satırları seç sonra ,koy 0 sütun seç
  
m[:,4]

m[0,:] # 0.satır bütün oradaki bütün sutunlar

m[0:2,0:3]#0 dan 2 ye kadar satırları al 0 dan 3 e kadar sutunları al

m[::,:2]# tüm satırları al , sutunları 2 tanesini al

m[1:3,0:2]
