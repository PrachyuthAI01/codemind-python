str1=input()
sum_digit = 0
for x in str1:
    if x.isdigit() == True:
        z = int(x)
        sum_digit = sum_digit + z

print(sum_digit)