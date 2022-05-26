def bin(s):
    p=''
    while(s>0):
        r=s%2
        s=s//2
        p+=str(r)
    return p[::-1] 
        
n=int(input())
s=c=0
while(n):
    v=n%10
    s+=v*pow(8,c)
    c+=1
    n=n//10
print(bin(s))