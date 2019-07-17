from numpy import concatenate
from numpy import matrix
from numpy import linalg

a = matrix( [[4,2,5],[2,5,8],[5,4,3]])          # Creas una matirz
b = matrix( [[60.7],[92.9],[56.3]] )            # Creas la columna delvector.
c =concatenate([a,b],axis=1)                    # Creas la fila del vecctor

print (a.T)                                    # transposicion de "a"

print (a*b)                                    # Multiplicacion de vectores a*b

print (a.I)                                    # Inverso de "a"

print (linalg.solve(a, b))                    #inverso de "a"
#import ramdom
c = int(-1)
