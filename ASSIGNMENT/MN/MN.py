#Remove character at even indices of a string

s=input("Enter the string")
print("String :",s[1::2])

# sort elements in a list without using built in function sort()

lst=input("Enter the list").split()
newlst=list(map(int,lst))
for i in range(0,len(newlst)-1):
    for j in range(0,len(newlst)-1):
        if newlst[i]<newlst[j]:
            newlst[i],newlst[j]=newlst[j],newlst[i]
print(newlst)