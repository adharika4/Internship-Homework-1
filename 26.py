# QUESTION 26
str45 = str(input("enter : "))
prefix  = char(input())
suffix = char(input())
if(str45[0] == prefix & str45[len(str45)-1] == suffix):
    print("perfect")
else:
        print("not perfect")