v=int(input())
l=1
while(v):
    p=v%10
    if(p>l):
        l=p
    v=v//10
print(l)
        