#count number of words in a string
s=input("Enter the string")
c=0
for i in s:
    if i==" ":
        c=c+1
print("Number of words",c+1)