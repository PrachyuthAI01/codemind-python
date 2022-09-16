n=int(input())
a=list(map(int,input().split()))
d=[]
a=set(a)
a=list(a)
for i in a:
    if i==0:
        continue
    elif i%2==0 and a.count(i)==1 and i not in d:
        d.append(i)
print(len(d))