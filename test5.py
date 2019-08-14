from numpy import*
a= array([[4,2,5],[2,5,8],[5,2,4]],float)
b= array([[5],[6],[7]],float)
linalg.det(a)
x =dot(linalg.inv(a),b)
print(x)

r=dot(a,x)
print(r)
