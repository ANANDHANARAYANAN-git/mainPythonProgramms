#Find largest element in a list without using any built in function
# lst=[3,1,7,9,5]
# lrg=0
# for i in lst:
#     if i>lrg:
#         lrg=i
# print("large value in list is",lrg)

lst=input("Enter the list element").split()   #because all element in list in form of string
lrg=0
for i in lst:
    if int(i)>lrg:                          #so value of i in the list must be specially mentioned as integer(int)
        lrg=int(i)
print("large value in list is",lrg)