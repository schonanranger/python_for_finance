import math
from numpy import *
import numpy as np
from time import time
#import random
random.seed(20000)
t0 = time()

S0 = 100.;K = 105.;T = 1.0;r = 0.05;sigma = 0.2;M = 50;dt = T / M;I = 250000

S = S0 * exp(cumsum((r - 0.5 * sigma ** 2) * dt + sigma * math.sqrt(dt)
                                                        *random.standard_normal((M+1,I)),axis = 0))
S[0] =S0
C0 = math.exp(-r * T) * sum(maximum(S[-1] - K, 0)) / I

tnp2 = time() - t0
print("European Option Value %7.3f" % C0)
print("Duration in Second %7.3f" % tnp2)

#matplotlib
import matplotlib.pyplot as plt
plt.plot(S[:,:10])
plt.grid(True)
plt.xlabel('time step')
plt.ylabel('index level')
plt.show()

plt.hist(S[-1],bins = 50)
plt.grid(True)
plt.xlabel('index level')
plt.ylabel('frequency')
plt.show()

plt.hist(np.maximum(S[-1] - K ,0), bins = 50)
plt.grid(True)
plt.xlabel('option inner value')
plt.ylabel('frequency')
plt.ylim(0,50000)
plt.show()