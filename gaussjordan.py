import numpy as np
def gaussjordan1(a,b):
    n=len(b)
    c=np.concatenate([a,b],axis=1)
    for e in range(n):
        t=c[e,e]
        for j in range(e,n+1):
            c[e,j]=c[e,j]/t
        for i in range(n):
            if i!=e:
                t=c[i,e]
                for j in range(e,n+1):
                    c[i,j]=c[i,j]-t*c[e,j]
    x=c[:,n]
    return x

def gaussjordan2(a,b):
    n=len(b)
    c=np.concatenate([a,b],axis=1)    #Con un print va a imprimir todo
    for e in range(n):
        c[e,e:]=c[e,e:]/c[e,e]
        for i in range(n):
            if i!=e:
                c[i,e:]=c[i,e:]-c[i,e]*c[e,e:]  #Con un print va a imprimir las sumas
    x=c[:,n]
    return x
