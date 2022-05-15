v=input()
p=v[0]
for i in range(len(v)):
    if(ord(p)<ord(v[i])):
        p=v[i]
print(p)
    