#find sum of multiple of 7 less than n

n=int(input("Enter the value"))
sum=0
for i in range(0,n,7):#or range (1,n), if i%7==0:
    sum=sum+i
print("sum is",sum)