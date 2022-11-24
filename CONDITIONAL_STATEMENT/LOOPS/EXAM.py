#find sum of multiple of 7 less than n

# n=int(input("Enter the value"))
# sum=0
# for i in range(0,n,7):#or range (1,n), if i%7==0:
#     sum=sum+i
# print("sum is",sum)

#Find the average of elements in a list

lst=input("Enter the number").split()
print(lst)
sum=0
n=len(lst)
for i in lst:
    sum=sum+int(i)
avg=sum/n
print("Average =",avg)