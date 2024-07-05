#birleştirme(concatenation)

import numpy as np 
x = np.array([1,2,3]) 
y = np.array([4,5,6])
z = np.array ([7,8,9])
np.concatenate([x,y,z])



# İki boyutlu bir NumPy dizisi oluşturma
a = np.array([[1, 2, 3], [4, 5, 6]])

# İki boyutlu diziyi concatenate kullanarak birleştirme
result1 = np.concatenate([a, a], axis=0)  # Satır bazında birleştirme
result2 = np.concatenate([a, a], axis=1)  # Sütun bazında birleştirme

print("Satır bazında birleştirme (axis=0):\n", result1)
print("Sütun bazında birleştirme (axis=1):\n", result2)
