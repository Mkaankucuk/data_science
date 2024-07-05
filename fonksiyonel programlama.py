#fonksiyonel programlama

#fonksiyonlar dilin baştacıdır daha esnek yapısı vardır
#(birinci sınıf nesnelerdir)
#yan etkisiz fonksiyonlar.(stateless,girdi-çıktı)
#yüksek seviye fonksiyonlar
#vektörel operasyonlar


#yan etkisiz fonksiyonlar (pure functions)

#ornek1: yan etki bağımsızlık
# def ile tanımladığımız fonksiyon dışarıdan etkilenebiliyorken
#def siz tnımladığımız fonksiyon dışardan hiçbir şekilde etkilenmez

A=9

def impure_sum(b):
    return b+A
    
    
def pure_sum(a,b):
    return a + b    

impure_sum(6)
pure_sum(3, 4)


#ornek2: olumcul yan etkiler 
#oop

# dosya açma ve dosya saydırmak için bir fonksiyon tanımladık
# 
def read(filename):
    with open(filename,'r') as f:
        return[line for line in f]

def count(lines):
    return len(lines)

example_lines= read('deneme.text')
lines_count = count(example_lines)
lines_count

#isimsiz fonksiyonlar (anonymous functions)
#lambda 
# lambda isimsiz fonksiyon oluşturmak için kullanılır kısa ve tek satırlık fonkiyonlar yazarken tercih edilir
# lambda argüman1,argüman2,...:ifade şekilde tanımlanır
#sorted sıralanabilir bir veri yapısını sıralamak için kullanılır
# lambda x: ne iş yapacağı , nerde yapsın

new_sum= lambda a,b: a + b
new_sum(4,5)

sirasiz_liste = [('b', 3 ),('a',8),('d',12),('c',1)]
sirasiz_liste 

sorted(sirasiz_liste,key = lambda x : x[1])


# vektorel operasyonlar 
# tek boyutlu liste vektör denir
# range aralık belirtme sayı dizisinde yineleme yapmak için kullanılır
# range(start,stop,step)
#for i in range(1, 10, 2):
#    print(i)
# Çıktı: 1 3 5 7 9

# bura oop
a = [1,2,3,4]
b = [2,3,4,5]

ab = []
range(0,len(a))



for i in  range(0,len(a)):
    ab.append(a[i]*b[i])
    
ab

# bura fonksiyonel programlama
# import numpy as np numpy isimli bir modülü bir kütüphaneyi çalışma dizinine dahil ettim
# as ile np kısayolu atadım

import numpy as np 
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b

# map & filter % reduce 
# fonksiyonlara fonksiyon olarak argüman olarak ekleme işlemi
# first class fonksiyonları bu fonksiyonlar iteratif nesneleri ve fonksiyonları argüman olarak alır
# işlemleri kolay hale getirir
# map fonksiyonu verilen bir vektörün içerisinde belirli bir fonksiyonu çalıştırma imkanı verir

liste = [1,2,3,4,5]

list(map(lambda x: x + 10,liste))



# filter 
# iteratif bir nesne alır bu nesne üzerinde başka bir iteratif nesne oluşturulur ve iteratif nesne içerisinde
# iteratif nesne içeisinde aranan şartlar filtrelenir
# şart aradı şarta baktı sağlayanları döndürdü bir işlem yapmadı


liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x % 2 == 0,liste))
# lambda listede 2 ye bölününce 0 mı diye true ya da false dedi dönücek true dönenleri listede orijinal şeilde dönecek şekilde gösterdi


#reduce 
# indirgeme işlemi yapar

from functools import reduce
# bu modül içerisinden bir kütüphane çağırmak

liste = [1,2,3,4]

reduce(lambda a,b : a + b , liste) 

# modul olusturmak
# belirli amaçları yerine getirmek için kullanılan fonksiyonlar topluluğudur 

# başka bir saydafa oluştur import sayfaismi sayfaismi.fonksiyonuayaz işleme sok
# from ile ordan al
#as kısaltma


# hatalar / istisnalar ( exceptions)
# bazı hataları gözlendiğinde programı durdurma çalışmaya devam et
# demenin yoludur
# dene hatanın kodu çalıştırmayı dene

a=10
b=0 

a/b

try:
    print(a/b)
except ZeroDivisionError:
    print("payda da sıfır olmaz")

# tip hatası

a = 10
b = "2"

a/b

try:
    print(a/b)
except TypeError:
    print("sayi ve string probllemi")




a = 10
b = 2

a/b

try:
    print(a/b)
except TypeError:
    print("sayi ve string probllemi")




















