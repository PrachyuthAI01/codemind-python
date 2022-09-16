n=int(input())
a=list(map(int,input().split()))
c=0
a=set(a)
a=list(a)
for i in a:
    if a.count(i)==1:
        c+=i
print(c)