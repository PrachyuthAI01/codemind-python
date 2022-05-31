n=int(input())
m=list(map(int,input().split()))
d=[]
s=[]
for i in range(len(m)//2,len(m)):
    d.append(m[i])
for i in range(len(m)//2):
    s.append(m[i])
d.reverse()
print(*(d+s))