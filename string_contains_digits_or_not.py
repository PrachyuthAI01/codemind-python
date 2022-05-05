c=int(input())
while(c>0):
    n=input()
    d=0
    for i in n:
        if(i.isdigit()):
            d+=1
    if(d>0):
        print("Yes")
    else:
        print("No")
    c-=1