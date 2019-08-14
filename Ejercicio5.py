from Lineal import *
from numpy import *
a=array([[0.52,0.20,0.25],[0.30,0.50,0.20],[0.18,0.30,0.55]],float)
b=array([[60],[50],[40]],float)
x=array([[1],[1],[1]],float)
[x,k]=jacobim(a,b,x,0.001,20)
print(x)
print("")
print(k)
