n=int(input())
a=list(map(int,input().split()))
d=[]
for i in a:
    s=str(i)
    s=s[::-1]
    d.append(int(s))
print(*d)