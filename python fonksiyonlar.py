#FONKSİYONLARA GİRİŞ - FONKSİYON OKURYAZARLIĞI
# fonksiyon bazı görevleri yerine getirmeye yarayan işleçler

#matematiksel işlemler
4*4
4/4
5-1
6+3
3**2    #kare alma


# fonksiyon nasıl yazılır
# fonsiyon def fonksiyon (ismi kullanılacak argüman) enter ile ne yapılacağını anlat
#def isim kullanılacak argüman : yapılacak işlem
4**2

def kare_al(x):
  print(x**2)
  
kare_al(3)

#print ile yapılan işlemde değişkenler aynı türde olması gerekir


def kare_al(x):
    print("girilen sayının karesi:" + str(x**2))
    
    kare_al(3)
    
def kare_al(x):
    print("girilen sayi:" + str(x) + ",karesi: " + str(x**2))
kare_al(3)    

#iki argümanlı fonksiyon tanımlamak
#alt enter deyince fonksiyon etkisinden kutulur
def kare_al(x):
    print(x**2)


def carpma_yap(x,y):
    print(x*y)
        
    
carpma_yap(2, 3)   
    
    
#ön tanımlı argümanlar
#öndecen argümanlara değer verebiliyoruz

def carpma_yap(x,y=1):
    print(x*y)
carpma_yap(3)    
    
#argümanların sıralanması   
#sıralamadan bağımsız tanımlanabilir
 def carpma_yap(x , y = 1):
     print(x*y)
     
carpma_yap(y=2,x=3)     
     
#ne zaman fonksiyon yazılır?
# fonksiyonlar uzun işlemleri ve tekrar eden işlemlerde kullanılır

#isi,nem,sarj

def direk_hesap(isi,nem,sarj):
    print((nem+isi)/sarj)
direk_hesap(25, 35, 70)

# fonksiyonların çıktısını girdi olarak  tanımlamak = return
# fonksiyonu tekrar işleme sokabilmek için return kullanılır 
#fonksiyon return ifadesine gelince durur returnun aşağısındaki ifadelerle ilgilenmez
#örnek çıktı diye tanımlasak cıktı diye yazdırır
def direk_hesap(isi,nem,sarj):
    print((nem+isi)/sarj)

cikti = direk_hesap(25, 35, 70)
cikti
print(cikti)
direk_hesap(25, 40, 70)*9


def direk_hesap(isi,nem,sarj):
    return(isi+nem)/sarj

cikti = direk_hesap(25,40,70)
cikti
print(cikti)
direk_hesap(25,40,70)*9

     
#local ve global değişkenler
# =============================================================================
# x=10
# y=10 global hepsini etkileyen değişkenler 
# =============================================================================
#def ile yapılan işlem ise local yerel işlemdir
 
    
#local etki alanından global etki alanına değiştirmek
# python ilk olarak local etki alnına bakar değişkenleri arar tarar bulmaya çalışır 
#localde bulamazsa global etki alanına geçecek
    
x=[]     
    
def eleman_ekle(y):
    x.append(y)
    print(str(y) + "ifadesi eklnedi")    
    

eleman_ekle("ali")
eleman_ekle("veli")    
x
    
#karar & kontrol yapıları 
#true - false sorgulamaları
#== mi denk mi diye sorgular

sinir= 5000
sinir==4000
sinir==5000

# if = eğer
# if den sonra işlem true ise şart sağlanır 
sinir = 50000
gelir = 40000

if gelir < sinir:
    print("gelir sinirdan kucuk")
    print(gelir*2)


# else = değilse 

sinir = 50000
gelir = 35000

if gelir > sinir:
    print("gelir sinirdan büyük")
        
else:
    print("gelir sinirdan küçük")    


sinir=50000
gelir=51000

if gelir== sinir:
    print("gelir sinira eşittir")
else:
    print("gelir sinira eşit değildir")

#elif değilse ama böyleyse

sinir = 50000
gelir1= 60000
gelir2= 50000
gelir3= 35000

if gelir1> sinir:
    print("tebrikler, hediye kazandiniz.")
    
elif gelir1< sinir:
        print("uyarı!")    
else:
    print("takibe devam")
    
    
#mini uygulama
# kullanıcıdan gelen bilgiler hep string olarak gelir değerimiz int ise başın aint yazmamız gerekir

sinir=50000
magaza_adi=input("mağaza adi nedir?: ")    
gelir = int(input("gelirinizi giriniz:"))    
    
if gelir > sinir:
    print("tebrikler:"+ magaza_adi + "promosyon kazandınız!")
    
elif gelir< sinir:
    print("uyarı! cok dusuk gelir:"+ str(gelir))
else:
    print("takibe devam")



#donguler - for
# listelere tek tek gidip işlem yapan uygulamalardır
# for da kullanılan i geçici değişken her bir değişkeni gezmek için kullanılır

# for   bu elemanları temsil eden değer  nerde yapılacağı :
# for da temsili bir değişken yazmamızın sebebi daha kolay bir şekilde işleme sokabilmek
    ogrenci = ["ali","veli","isik","berk"]

for i in ogrenci :
    print(i)


maaslar = [1000,2000,3000,4000,5000]
for i in maaslar:
    print(i)


# döngü ve fonksiyonları birlikte kullanmak

# maaslara yuzde 20 zam yapılacak gerekli kodu yaz
# dongu yazılacak
# fonksiyon yazılacak
# for un i si x gibi davranıp işleme girecek
# print fonksiyonunu kullanmayıyımda kendi yazdığım fonksiyonu kullanayım
maaslar= [1000,2000,3000,4000,5000]

def yeni_maas(x):    
    print(x*20/100+ x)

for i in maaslar:
    yeni_maas(i)


# mini uygulama
# if, for ve fonksiyonları birlikte kullanmak
#maası 3000 tl altına %20 zam üstüne %10 zam

maaslar= [1000,2000,3000,4000,5000]

def maas_ust(y):
    print(y*10/100+y)

def maas_alt(z):
    print(z*20/100+z)

for i in maaslar:
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)


#break & continue
# break istediğimiz değere geliyorsa döngüyü durdur
#contiune yazdığımız değeri atlıyor geç diyor

maaslar=[8000,5000,2000,1000,3000,7000,1000]
maaslar.sort()
maaslar
  
for i in maaslar:
    if i ==3000:
        print("kesildi")
        break 
print(i)        


for i in maaslar:
    if i == 3000:
        continue
print(i)        

#while
# sayi += 1 üzerine 1 değeri ekleyip yeniden ata

sayi = 1
while sayi < 10:
    sayi += 1  
    print(sayi)





def harf_say(x):
    len(x)
harf_say("merhaba!")



  