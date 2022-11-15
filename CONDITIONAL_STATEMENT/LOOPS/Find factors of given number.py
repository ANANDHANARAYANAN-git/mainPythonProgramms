#find factors of given number,devided by this number reminder is 0.
# n=int(input("enter the number"))
# for i in range(1,n+1,1):
#     if n%i==0:
#         print(i,end=" ")

#count number of factors

# n=int(input("enter the number"))
# c=0
# for i in range(1,n+1,1):
#     if n%i==0:
#         c=c+1
# print("Number of factors",c)
#both
n=int(input("enter the number"))
c=0
for i in range(1,n+1,1):
    if n%i==0:
        c=c+1
        print(i,end=" ")
print("\nNumber of factors",c)

