from Lineal import *
from numpy import *
a=array([[1,1/2,1/3],[1/4,1/5,1/6],[1/7,1/8,1/9]],float)
b=array([[4],[5],[6]],float)
x=array([[1],[1],[1]],float)
[x,k]=gaussidelm(a,b,x,0.01,500)
print(x)
print("")
print(k)
