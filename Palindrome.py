v=int(input())
r=0
t=v
while(v):
    l=v%10
    r=r*10+l
    v=v//10
if(t==r):
    print("True")
else:
    print("False")

