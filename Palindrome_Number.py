n=int(input())
#a=list(map(int,input().split('
')))
while (n!=0):
        a=int(input())
        t=a
        r=0
        while(a):
            d=a%10
            r=r*10+d
            a=a//10
        
        if(t==r):
            print(True)
        else:
            print(False)
