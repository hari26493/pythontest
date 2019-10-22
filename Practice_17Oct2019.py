"""
def solution(A):
    # write your code in Python 3.6
    m=max(A)
    l=[]
    j=range(1,m+1)
    if m>0:
        for i in j:
            if (i not in A) and i>0:
                l.append(i)
            elif i<0:
                l.append(1)
            else:
                l.append(m+1)
    else:
        l.append(1)

    l.sort()
    return l[0]

print(solution([-1,-2,3,1,2,5]))
"""
from math import *
print(sqrt(6561))
def sollution(n1,n2):
    d={}
    for i in range(n1,n2+1):
        x=sqrt(i)
        cn=0
        while True:
            xx=str(x)
            if xx[-2:]=='.0':
                xx=int(xx[0:xx.index('.')])
                if isinstance(xx,int):
                    cn=cn+1
                    x=sqrt(xx)
                    d[i]=cn
            else:
                break
    v=d.values()
    ma=max(v)
    return ma

print(sollution(6000,7000))