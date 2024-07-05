# nesne yonelımlı programlama

#işlemleri kolaylaştırmak ve optimize etmek

#sınıf= benzer özellikler,ortak amaçlar taşıyan,içerisinde metod ve değişkenler olan yaılardır
# bazı fonksiyonlar yazdık bazı özellikleri aynı aynı özellikleri erişmek için kullanılır
# 


    
 # sınıf özellikleri(class attributes
 
 #sınıf özelliklerine erişmek istiyorsak sınıf.özellikle erişebiliriz

 class Veribilimci():
    self.bolum = " "
     sql = "evet"
     deneyim_yılı = 0
     self.bildiği_diller = []
     
#sınıfların özellikleri erişmek
Veribilimci.bolum
Veribilimci.sql     

#sınıfların özelliklerini değiştirmek
Veribilimci.sql="hayır"
Veribilimci.sql


#SINIF ÖRNEKLEMESİ 
# atadığımız kişi veribilimci özelliklerini alır
ali = Veribilimci()
ali.sql
ali.bildiği_diller.append("python")
# alide değiştirdiğimiz şey velidede etkiledi
veli = Veribilimci()
veli.sql
veli.bildiği_diller

#ornek ozellikleri
#__init__ (self) :
# self.bildiği diller = herbir örnek kendi içinde değişebilir dedik    
#self.özellik aşağıda değiştirirsn sadece değştirdiğin kişide değişir
class Veribilimci ():
    def __init__(self):
        self.bildiği_diller=[]

ali = Veribilimci()
ali.bildiği_diller


ali.bildiği_diller.append("python")
ali.bilidiği_diller

veli.bildiği_diller
veli.bildiği_diller.append("r")
veli.bildiği_diller


Veribilimci.bolum
ali.bolum="istatistik"
Veribilimci.bolum
veli.bolum
veli.bolum="end_muh"
veli.bolum
ali.bolum


#ornek metotları 

class veribilimci():
    calısanlar=[]
    def __init__(self):
        self.bildiği_diller=[]
        self.bolum = ""
def dil_ekle(self,yeni_dil):
    self.bilidiği_diller.append(yeni_dil)

ali = veribilimci()
ali.bildiği_diller
ali.bolum

veli= veribilimci()
veli.bildiği_diller
veli.bolum




#miras yapıları(inheritance)
# bir class tanımla başka bir class olacak aynı özellikler barındıracak o özellikleri kullanak için class kullanılabilecek
# mevcut yapıları kullanma
#tanımlı class a () içine class adını yazıp özelliklerini kullanma

class employess():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address  = ""


class datascience(employess):
    def __init__(self):
        self.programming = ""
        
    
veribilimci1 = datascience()        
    
        
        
class marketing(employess):
    def __init__(self):
        self.stroytelling = ""

mar1 = marketing()

























