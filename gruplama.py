# gruplama işlemi 
import pandas as pd
import seaborn as sns


df= pd.DataFrame({'gruplar':['A','B','C','A','B','C'],
                  'veri':[10,11,52,23,43,55]},columns=['gruplar','veri'])
df

df.groupby("gruplar") # dateframe git groupby fonksiyonu  ile gruplar değişkenini yakala gruplar değişkenindeki katogeri sınıflarını  tut
 
df.groupby("gruplar").mean() # grupların ortalamasını al

df.groupby("gruplar").sum() # grupların toplamı

df = sns.load_dataset("planets")
df.head()
df.groupby("method") # methodu yakala

df.groupby("method")["orbital_period"].mean() #öncelikle gruplama yapacağı değişkeni ifade ettik grupladıktan sonra ne yapılacağını yazmamız gerekir

# method katogarik değişken birçok sınıf var bu sınıfları grouby diyince gitti yakaladı bu gruplara karşılık gelen orbital_period değişkenini yakaladı ve ortlamasını aldı
