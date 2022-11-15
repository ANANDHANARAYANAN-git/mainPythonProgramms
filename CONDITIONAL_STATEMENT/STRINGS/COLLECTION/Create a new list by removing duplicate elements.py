#create a new list by removing duplicate elements
lst=[1,2,2,3,3,3,3,4,4,4,5,5]
newlst=[]
for i in lst:
    if i not in newlst:
        newlst.append(i)
print(newlst)
