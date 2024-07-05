# Nesne Yönelimli Programlama (OOP)
# İşlemleri kolaylaştırmak ve optimize etmek için kullanılır.
# Sınıf: Benzer özellikler taşıyan, ortak amaçlar taşıyan, içinde metod ve değişkenler barındıran yapılardır.

# Sınıf Özellikleri (Class Attributes)
# Sınıf özelliklerine erişmek istiyorsak sınıf.özellik şeklinde erişebiliriz.

class Veribilimci:
    bolum = " "
    sql = "evet"
    deneyim_yılı = 0
    bildiği_diller = []

# Sınıf özelliklerine erişmek
print(Veribilimci.bolum)  # Çıktı: 
print(Veribilimci.sql)    # Çıktı: evet

# Sınıf özelliklerini değiştirmek
Veribilimci.sql = "hayır"
print(Veribilimci.sql)    # Çıktı: hayır

# Sınıf Örneklemesi
# Atadığımız kişi Veribilimci özelliklerini alır
ali = Veribilimci()
print(ali.sql)            # Çıktı: hayır
ali.bildiği_diller.append("python")
print("Ali'nin bildiği diller:", ali.bildiği_diller)  # Çıktı: Ali'nin bildiği diller: ['python']

# Ali'de değiştirdiğimiz şey Veli'de de etkiledi
veli = Veribilimci()
print(veli.sql)           # Çıktı: hayır
print("Veli'nin bildiği diller:", veli.bildiği_diller)  # Çıktı: Veli'nin bildiği diller: ['python']

# Bu sorunu çözmek için örnek değişkenleri kullanmalıyız
class Veribilimci:
    def __init__(self):
        self.bolum = " "
        self.sql = "evet"
        self.deneyim_yılı = 0
        self.bildiği_diller = []

# Sınıf Örneklemesi
ali = Veribilimci()
print(ali.sql)  # Çıktı: evet
ali.bildiği_diller.append("python")
print("Ali'nin bildiği diller:", ali.bildiği_diller)  # Çıktı: Ali'nin bildiği diller: ['python']

veli = Veribilimci()
print(veli.sql)  # Çıktı: evet
print("Veli'nin bildiği diller:", veli.bildiği_diller)  # Çıktı: Veli'nin bildiği diller: []

# Veribilimci sınıfının sınıf özelliklerine erişim
print(Veribilimci.bolum)  # Çıktı: 
ali.bolum = "istatistik"
print(Veribilimci.bolum)  # Çıktı: 
print(veli.bolum)         # Çıktı: 

veli.bolum = "end_muh"
print(veli.bolum)         # Çıktı: end_muh
print(ali.bolum)          # Çıktı: istatistik
