n=int(input())
a=list(map(int,input().split()))
d=[]
for i in a:
    if a.count(i)==i and i not in d:
        d.append(i)
print(len(d))
