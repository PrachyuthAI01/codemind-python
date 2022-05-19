n=int(input())
a=0
b=1
r=0
for i in range(1,n+1):
    print(a,end=' ')
    r=a+b
    a=b
    b=r