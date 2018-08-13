import numpy as np
import random
r = np.random.standard_normal((4, 3))
s = np.random.standard_normal((4, 3))
#print(r)
#print(s)
#print(r+s)

s = np.ones((4,3))
print(s)
s = s * 2 + 3
print(s)
r = np.ones((4,3))
print(r+s)
z = np.random.standard_normal(3)
print(z+s)
x = np.random.standard_normal(4)
print(x+s.T)