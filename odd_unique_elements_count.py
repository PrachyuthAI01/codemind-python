n=int(input())
a=list(set(map(int,input().split())))
d=[]
for i in a:
    if i%2!=0 and a.count(i):
        d.append(i)
print(len(d))