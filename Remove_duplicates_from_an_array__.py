m=int(input())
n=list(map(int,input().split()))
s=[]
for i in range(0,len(n)):
    for j in range(0,len(n)):
        if(n[i]==n[j]):
            s.append(n[i])
d=set(s)
print(*d)