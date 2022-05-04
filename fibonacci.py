n=int(input())
n1=0
n2=1
a=0
print(n1,n2,end=' ')
for i in range(n-2):
    a=n1+n2
    print(a,end=' ')
    n1=n2
    n2=a