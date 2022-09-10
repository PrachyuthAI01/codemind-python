n=int(input())
a=list(map(int,input().split()))
d=int(input())
c=0
for i in a:
    if i<=d:
        c+=i
print(c)