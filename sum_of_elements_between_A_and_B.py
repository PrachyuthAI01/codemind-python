n=int(input())
a=list(map(int,input().split()))
k,l=map(int,input().split())
c=0
for i in a:
    if l>=i and k<=i:
        c=c+i
print(c)