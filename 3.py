# QUESTION 3
num = int(input("enter num : "))
fac = 1
for i in range(0,num+1):
    fac = fac * (num-i)
    print(fac)