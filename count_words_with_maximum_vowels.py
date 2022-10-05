s=str(input())
s=s.split(' ')
a=[]
v='aeiou'
for i in s: 
    c=0
    for j in i: 
        if j in v:
            c+=1
    a.append(c)
print(a.count(max(a)))