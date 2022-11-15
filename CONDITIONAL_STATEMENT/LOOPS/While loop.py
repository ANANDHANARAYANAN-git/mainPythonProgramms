#While loop
# i=1#star
# while i<=5:#condition
#     print(i)
#     i=i+1#increment

#Find the sum of even number lesss than n using while loop
# n=int(input("Enter the number"))
# sum=0
# i=2#start(1st step)
# while i<=n:#condition(3 step)
#     sum=sum+i
#     i=i+2#increment(2nd step)
# print("Sum is",sum)

#find sum of odd numbers and even number upto n using while loop
n=int(input("Enter the number"))
esum=0
osum=0
i=1
while i<=n:
    if i%2==0:
        esum=esum+i
    else:
        osum=osum+i
    i=i+1
print("Sum of odd numbers",osum)
print("sum of even numbers",esum)
