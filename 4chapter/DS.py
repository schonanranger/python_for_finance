import numpy as np
dt = np.dtype([('Name','S10'),
               ('Age','i4'),
               ('Height','f'),
               ('Children/Pet','i4',2)])
s = np.array([('Smith',45,1.83,(0,1)),
              ('Jones',53,1.72,(2,2))],dtype = dt)
print(s['Age'])
print(type(s))