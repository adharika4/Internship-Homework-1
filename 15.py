# QUESTION 15
p= open('C:/Users/dell/Downloads/internship homework/file.csv','r',newline='')
empdata = csv.reader(p)
for r in empdata:
    print(r)