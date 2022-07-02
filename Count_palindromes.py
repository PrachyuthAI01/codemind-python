n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    s=str(i)
    if(s==s[::-1]):
        c+=1
print(c)