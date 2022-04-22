p=int(input())
r=0
while(p):
    v=p%10
    r=r*10+v
    p=p//10
print(r)