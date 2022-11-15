#find sum of even numbersup to n
n=int(input("enter the limit"))
sum=0
for i in range(2,n+1,2):
    sum=sum+i
print("sum is",sum)

