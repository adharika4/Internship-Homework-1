# QUESTION 12
number = int(input("enter : "))
sum = 0
while(number>0):
    val =number%10
    sum += val
    number = number / 10
print(sum)