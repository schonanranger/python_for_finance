


import numpy as np
a = np.array([0.,0.5,1.0,1.5,2.0])
dt = np.dtype([('Name','S10'),('Age','i4'),('Height','f'),('Children/Pets','i4',2)])
s = np.array([('Smith',45,1.83,[0,1]),
              ('Jones',53,1.72,[2,2])],dtype = dt)
print(s)