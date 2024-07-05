#toplulaştırma ve gruplama ( aggregation & grouping)

# basit toplulaştırma fonksiyonları 
# count() 
# first()
# last()
# mean()
# median()
# min()
# max()
# std()
# var()
# sum()

import seaborn as sns #seaborn kütüphanesi

df= sns.load_dataset("planets") #veri seti yükle
df.head()

# =============================================================================
#  method  number  orbital_period   mass  distance  year
# 0  Radial Velocity       1         269.300   7.10     77.40  2006
# 1  Radial Velocity       1         874.774   2.21     56.95  2008
# 2  Radial Velocity       1         763.000   2.60     19.84  2011
# 3  Radial Velocity       1         326.030  19.40    110.62  2007
# 4  Radial Velocity       1         516.220  10.50    119.47  2009
# =============================================================================

df.shape #(1035, 6)

df.mean() #ortalama fonksiyonu bütün değişkenler için ayrı ayrı ortalama alıyor

df["mass"].mean() #2.6381605847953216 bir değişken için ortalama aldı

df.count() # değerleri saymak için kullanılır

df["mass"].std() # standart sapma için
df["mass"].var() # varyansını bulmak için

df.describe() # veri seti içindeki bütün betimsel istatistiklerini alır


df.describe().T # gösterimin tersini al

df.dropana().describe().T #veri setinde eksik değler varsa yazılır onları çıkartıp hesaplar
