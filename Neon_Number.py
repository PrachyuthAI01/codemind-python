v=int(input())
p=v*v
r=0
while p>0:
    r=r+p%10
    p=p//10

if (v==r):
    print("Neon Number")
else:
    print("Not Neon Number")