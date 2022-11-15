#Count number of vowels in a sring and print it
s=input("Enter he string")
c=0
for i in s:
    if i in "aeiouAEIOU":
        print(i,end=" ")
        c=c+1
print("\nnumber of vowels",c)