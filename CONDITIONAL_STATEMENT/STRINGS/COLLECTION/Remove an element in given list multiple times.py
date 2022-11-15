#remove an element in given list multiple time.
lst=[4.6,1,1,1,1,2,4.6,3,4.6,4,5,6,7,8,4.6,]
for i in lst:
    if i==4.6:
        lst.remove(i)        #it cannot remove multiple elements in near position.
print(lst)