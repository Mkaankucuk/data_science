# import numpy ile numpy kütüphanesi çağırılır
# as ile kısayol olarak  atanır


# neden numpy 
# karmaşık işlemleri basite indirger
#  .array numpy kütüphanesinden array şekilde 
# çagırlamasını saglar   
#  daha performanslı bir veri tutma sağlar
# optimizasyon ve yazılımsal anlamda iyilestirme sunmuştur

# tek boyutlu vektör iki boyutlu matris tir
# numpy arrayi olusturma

import numpy  as np
np.array([1,2,3,4,5])

a =  np.array([1,2,3,4,5])
type(a)

np.array([3.14,4,2,13]) #sabit tip tutar

np.array([3.14,4,2,13],dtype = "int") #sabit tipi int olarak ayarla

# sıfırdan array olusturma

np.zeros(10,dtype = int) # zeros 10 ile 10 tane sıfır olusturdu

np.ones((3,5)) # ıkı boyutlu bır dızı olusturdu

np.full((3,5),3) # ıkı boyutlu bır dızıde butun sayılar 3 olsun dedı 

np.arange(0,31,3) # 0 dan 31 e kadar 3 erli sekılde sırala

np.linspace(0,1,10) # 0 ile 1 arasında değer oluştur

np.random.normal(10,4,(3,4)) #ortalamsı 10 standart sapması 3 e 4 lük bir dizinin rastgele oluşruması
# istediğimiz bir dağılım özelliğini kullanabiliriz

np.random.ranint(0,10,(3,3)) #int değerlerden rastgele şekilde değer oluşturmak istiyorum dersek kullanılır
