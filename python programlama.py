#SAYILAR VE STRINGLERE GIRIS
9 
9.2
9+9
9*9

print("hello aı era")
#type kodu değişkein hangi türde olduğunu belirtir

type(9) 

type(9.2)

#STRINGLERE YAKINDAN BAKALIM "" '' BU İŞARETLERİ ALGILAR
type("123")

"a" + "b"
#" boşluk olarak algılıyor

"a"*3
#STRING METODLARI -LEN

gel_yaz= "geleceğe yazanlar"

a = 9
b = 10
a*b

#"a"+"b"#kodun çıktısı 'ab'
#"9"+"1"#kodun çıktısı '91'
#"10"+2#işlem hatası
#boşlukta bir karakter olarak sayılır

len(gel_yaz) #string değerin kaç harf olduğunu gösterir

#STRING METODLARI - UPPER () VE LOWER()
#STRING YAZILDIKTAN SONRA. KOYULARSA O STRİNGE METOT UYGULANACAĞI AKLNIA GELİR
#UPPER STRING İ BÜYÜK HARFE LOWER KÜÇÜK HARFE ÇEVİRİ
#islower ve isupper büyük mü küçük mü diye kontrol eder true ya da false yazar
#metotlardan sonra ( ) konur
gel_yaz.upper()
gel_yaz.lower()
gel_yaz.islower()

B = gel_yaz.upper()
B.islower()

#STRING METOTLARI -replace()
# replace harfleri neyi neyle değiştireceğini söyler

gel_yaz.replace("e", "a")

#strıng metotları- strip()
# strip() istenmeyen karakterleri kırpmak için kullanılır

gel_yaz ="geleceği_yazanlar"
gel_yaz.strip()

gel_yaz= "*geleceği_yazanlar*"
gel_yaz.strip()

gel_yaz="lgeleceğe_yazanlarl"
gel_yaz.strip("l")

#METOTLARA GENEL BAKIŞ
#dir() yazıp kodu içine yazarsak uygulanabilecek metotlar gözükür

gel_yaz.capitalize()
gel_yaz.title()


#SUBSTRİNG ELİMİZDEKİ STRİNGLERİN ALT KÜMESİNE ERİŞMEK İÇİN KULLANILIR
#[] köşeli parantezden önceki kodda bir seçim işlemi olacak
#[0:3]YAZARSAK 0 DAN 3 E KADAR HARFLERİ ALIR
gel_yaz= "geleceği yazanlar "

gel_yaz[0]
gel_yaz[20]
gel_yaz[0:3]

gel_yaz[3:7]

#DEĞİŞKENLER

a = 9
b = "ali_uzaya_git"
c = a*2
a/c

#TİP DONUŞÜMLERİ 
# input() kullanıcıdan bilgi almak
#eğer toplamabir toplamiki  diye toplarsan string olarak toplar yanyana yazar ama sayı olarak toplamak istiyorsak int yazıcaz,
# str(12) değersek string olrak dönüştürür
# float(12) dersek 12.0 diye ondalıklı çıkarır

toplama_bir = input()

toplama_iki = input()
int(toplama_bir) + int(toplama_iki)
float(12)
int(12.0)
str(12)
#print( ) fonksiyonu
# sep= "_" boşluklar arası _ koyar
# fonksiyonların genel amaçlarını biçimlendirmek için kullanılan alt görev belirticilerine argüman denir
# mesela sep bir argümandır 
#?print yazınca kullanılacabilecek argümanlar ortaya çıkar 
print("geleceği","yazanlar",sep="_")

#VERİ YAPILARI 

#LİSTELER 
#[ ] veya list() ile liste oluşturabiliyoruz

notlar=[90,80,70,50]

type(notlar)

liste_genis=["a",19.3,90,notlar]

len(liste_genis)

liste_genis[0]
# del kodu siler

#LİSTELER - ELEMAN İŞLEMLERİ 
#listelerde eleman seçme [0:2] 0 dan 2 ye kadar olarak algılanır [:2] 0 dan 2 ye kadar [2:] 2 den sona kadar 
#liste içerisndeki listeyi seçersen içindeki listeyi tamamen alır
#liste içerisindkei listedeki elemanı almak istiyorsan [][]yapman gerekir
liste= [10,20,30,40,50]
liste[1]
liste[:2]
liste[2:]

yeni_liste= ["a",10,[20,30,40,50]]
yeni_liste[2]
yeni_liste[2][1]

#LİSTELER - ELEMAN DEĞİŞTİRME 
# []SEÇ BAŞKA BİR STRİNG YAZ
#listeye yeni bir eleman eklme liste=liste+["kemal"] diye eklenir
# listeden eleman silme  del liste1[2] elaman silnir

liste1=["ali","veli","berkcan","ayşe"]
liste1
liste1[1]="veli"

liste1=liste1+["kemal"]
liste1
del liste1[2]
liste1

#listeler - liste metodları 
#listeye eleman eklme liste.append("istediğin eleman") işlemi ile yapılır
#listeye eleman silme liste.remove() ile oluyor

liste2=["ali","veli","mert"]
liste2.append("berkcan")
liste2
liste2.remove("berkcan")
liste2


#listeye insert işlemi ile o indekse eleman ekliyoruz
#en sona eklemek için liste.insert(len(liste),"beren") şekilde yapılır
#listedeki o indeksi silme için kullalıcan metot poptur

liste2.insert(0,"ayşe")
liste2
liste2.pop(0)
liste2

#listede kaç tane olduğunu söylemek için count metodu kullanılır
liste3=["ali","veli","mert","ali","veli"]
liste3.count("ali")
liste3.count("veli")
liste3.count("mert")

# copy listeyi kopyalıyor

liste_yedek=liste3.copy()

#extend listeyi birleştirmek için kullanılır

liste3.extend(["a","b",10])
liste3

#index listedeki kaçıncı eleman olduğunu gösteriyor
liste3.index("ali")

#reverse listeyi ters çevirir
liste3.reverse()
liste3

#sort sıralama yapmak için kullanılır

liste4=[4,3,7,9]
liste4.sort()
liste4
#clear listeyi temizlemek için kullanılır


#VERİ YAPILARI - TUPLE
#KAPSAYICIDIR,SIRALIDIR,DEĞİŞTİRİLEMEZ
#listeler gibi veri yapısı
#tek elemanlıysa sonuna , konur

t=("ali","veli",1,2,3.2,[1,2,3,4])
t="ali","veli",1,2,3.2,[1,2,3,4,]
t=("eleman",)
type(t)

#tuple eleman işlemleri indeks seçme liste ile  aynı


#veri yapıları - dictionary(sözlük)
# kapsayıcıdır,sırasızdır,değiştirilebilir
# listedelerde olduğu gibi index işlemi yapılmaz
# ilk yazılan anahar sözcük ikkinci açıklaması
sozluk= {"reg":"regresyon modeli",
         "log":"logistik regresyon",
         "cart":"classification and reg"}
sozluk

len(sozluk)

sozluk={"reg":["rmse",10],
        "loj":["mse",20],
        "cart":["sse",30]}
sozluk

#SOZLUK ELEMAN İŞLEMLERİ
#sozlukte eleman çekmek için ör sozluk["reg"] diye çağırılır
sozluk["reg"]

sozluk= {"reg":{"rmse":10,
               "mse":20,
               "sse":30},
         
        "loj":{"rmse":10,
              "mse":20,
              "sse":30},
        
        "cart":{"rmse":10,
                "mse":20,
                "sse":30}}

sozluk

sozluk["reg"]["sse"]

#sozluk - eleman ekleme değiştirme 
#eleman eklerken sozluk dışına eklenecek eleman yazılır
#değiştirikken anahtar ifade ve değiştirilecek string yazılır

sozluk= {"reg":"regresyon modeli",
         "log":"logistik regresyon",
         "cart":"classification and reg"}
sozluk["gbm"]="gradient boosting mac"
sozluk
sozluk["reg"]="coklu doğrusal regresyon"
sozluk


sozluk[1]="yapay sinir ağları"
sozluk

#sozluğe liste eklenemez çünkü liste değiştirilebilir
#tuple sozluğe eklenebilir

t=("tuple",)
sozluk[t]="yeni bir şey"
sozluk

#veri yapıları -setler(kümeler)
#sırasızdır,değerleri eşsizdir,değiştirilebilir,farklı tipleri barındırabilir

s=set()
s
l=[1,"a","ali",123]
s=set(l)
s

t=("a","ali")

s=set(t)
s

ali= "lütfen_ata_bakma_uzaya_git"
type(ali)
s=set(ali)
s

l=["ali","lütfen","ata","bakma","uzaya","git","git","ali","git"]
l

s=set(l)
s

len(s)

#ctrl+4 yorum satırı
#ctrl+1 ile başına yorum satırı
#setlerde eleman ekleme çıkarma
#.add metoduyla eklenir
#.remove metoduyla silinir
l=["geleceği","yazanlar"]
s=set(l)
s
dir(s)
s.add("ile")
s
s.add("gelecege_git")
s
s.add("ali")
s
s.remove("ali")
s
# =============================================================================
# 
# setlerde - klasik küme işlemleri 
# difference() ile farkını ya da "-" ifadesi
# intersection() iki küme kesişimi ya da "&" ifadesi
# union() iki kümenin birleşimi
# symmetric_difference() ikiside olmayanları
# =============================================================================

# difference ilk başta olmayana göre set1 de olup set2 de olamyan

set1=set([1,3,5])
set2=set([1,2,3])

set1.difference(set2)
set2.difference(set1)

set1.symmetric_difference(set2)

set1-set2
set2-set1


set1=set([1,3,5])
set2=set([1,2,3])

set1.intersection(set2)
set2.intersection(set1)

kesisim = set1 & set2
kesisim

birlesim = set1.union(set2)
birlesim

set1.intersection_update(set2)
set1

#set sorgu işlemleri
#.isdisjoint iki kümenin kesişiminin bos olup olmadığının sorgulanması
#.issubset bir kümenin bütün elemanlarının baska bir küme içerisinde yer alıp almadığı
set1=set([7,8,9])
set2=set([5,6,7,8,9,10])

set1.isdisjoint(set2)

set1.issubset(set2)


































