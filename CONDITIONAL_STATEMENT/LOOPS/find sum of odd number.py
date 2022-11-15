#find sum of odd number up to n
n=int(input("Enter the limt"))
sum=0
for i in range(1,n+1,2):
    sum=sum+i
print("Sum is",sum)