# import numpy ile numpy k�t�phanesi �a��r�l�r
# as ile k�sayol olarak  atan�r


# neden numpy 
# karma��k i�lemleri basite indirger
#  .array numpy k�t�phanesinden array �ekilde 
# �ag�rlamas�n� saglar   
#  daha performansl� bir veri tutma sa�lar
# optimizasyon ve yaz�l�msal anlamda iyilestirme sunmu�tur

# tek boyutlu vekt�r iki boyutlu matris tir
# numpy arrayi olusturma

import numpy  as np
np.array([1,2,3,4,5])

a =  np.array([1,2,3,4,5])
type(a)

np.array([3.14,4,2,13]) #sabit tip tutar

np.array([3.14,4,2,13],dtype = "int") #sabit tipi int olarak ayarla

# s�f�rdan array olusturma

np.zeros(10,dtype = int) # zeros 10 ile 10 tane s�f�r olusturdu

np.ones((3,5)) # �k� boyutlu b�r d�z� olusturdu

np.full((3,5),3) # �k� boyutlu b�r d�z�de butun say�lar 3 olsun ded� 

np.arange(0,31,3) # 0 dan 31 e kadar 3 erli sek�lde s�rala

np.linspace(0,1,10) # 0 ile 1 aras�nda de�er olu�tur

np.random.normal(10,4,(3,4)) #ortalams� 10 standart sapmas� 3 e 4 l�k bir dizinin rastgele olu�rumas�
# istedi�imiz bir da��l�m �zelli�ini kullanabiliriz

np.random.ranint(0,10,(3,3)) #int de�erlerden rastgele �ekilde de�er olu�turmak istiyorum dersek kullan�l�r
