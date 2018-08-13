s = set(['u','d','du','du','d','du'])
t= set(['d','dd','u','uu'])
print(s,t)
print(s.union(t))
print(s.intersection(t))
print(s.difference(t))
print(t.difference(s))
print(s.symmetric_difference(t))
from random import randint
l = [randint(0,10) for i in range(1000)]
print(len(l))
print(l[:20])
print(set(l))