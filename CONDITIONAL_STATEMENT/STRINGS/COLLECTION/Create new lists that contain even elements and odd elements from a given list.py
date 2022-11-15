#create 2 list that contain even elements and odd elements

lst=[1,3,2,5,4,7,9,6]
elst=[]
olst=[]
for i in lst:
    if i%2==0:
        elst.append(i)
    else:
        olst.append(i)
print(elst)
print(olst)