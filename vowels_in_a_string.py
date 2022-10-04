s=str(input())
x=input()
for i in range(len(s)):
    if s[i]==x:
        print("True")
        print(i)
        break
else:
    print("False")