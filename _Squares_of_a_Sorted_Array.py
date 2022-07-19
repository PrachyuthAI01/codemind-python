n=int(input())
a=list(map(int,input().split()))
d=[]
for i in a:
    d.append(i**2)
d=sorted(d)
print(*d)