# pivot tablolar 
# veri setleri üzerinde bazı satır ve sutunlara işlemler yaparak amaca uygun hale getirir

import pandas as pd 
import seaborn as sns

titanic= sns.load_dataset('titanic')
titanic.head()

titanic.groupby("sex")["survived"].mean() # gruplama işlemi yapıcam cinsiyet e göre sürekli değişken olarak survived seçicem 

# =============================================================================
# sex
# female    0.742038
# male      0.188908
# =============================================================================

# dataframe olmasıı istiyorsak [] bir tane daha koyarız

titanic.groupby(["sex","class"])[["survived"]].aggregate("mean").unstack()
# =============================================================================
#   survived                    
# class      First    Second     Third
# sex                                 
# female  0.968085  0.921053  0.500000
# male    0.368852  0.157407  0.135447
#
# unstack tablonun eksenini değiştiriyor
# =============================================================================

# pivot ile table 
# odaklandığın değişken , index nedir , başka hangi değişkene odaklanmak istersin
titanic.pivot_table('survived' ,index="sex",columns= "class")

# =============================================================================
# class      First    Second     Third
# sex                                 
# female  0.968085  0.921053  0.500000
# male    0.368852  0.157407  0.135447
# =============================================================================

titanic.age.head()

# =============================================================================
# 0    22.0
# 1    38.0
# 2    26.0
# 3    35.0
# 4    35.0
# 
# =============================================================================

age= pd.cut(titanic["age"],[0.18,90])
age.head(10)

titanic.pivot_table("survived",["sex",age],"class")
#age ı burada dışarıdan aldık
# =============================================================================
# class                   First    Second     Third
# sex    age                                       
# female (0.18, 90.0]  0.964706  0.918919  0.460784
# male   (0.18, 90.0]  0.396040  0.151515  0.150198
# 
# 
# =============================================================================






