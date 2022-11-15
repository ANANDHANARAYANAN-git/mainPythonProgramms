# #count number of vowel in a string
# # str=input("Enter the string")
# # c=0
# # for i in str:
# #     if i in "aeiouAEIOU":
# #          print(i,end=" ")
# #          c=c+1
# # print("\nnumber of vowel",c)
#
# #count number of words of sentence
# # s=input("Enter the string")
# # c=0
# # for i in s:
# #      if i==" ":
# #           c=c+1
# # print(c+1)
#
#
# # i=1
# # while i<5:
# #      print(i)
# #      i=i+1
#
# # n narural numbers using while loop
#
# # n=int(input("Enter the number"))
# # i=1
# # while i <=n:
# #      print(i)
# #      i=i+1
#
# #find the sum of even number less than n
#
# # n=int(input("Enter the number"))
# # esum=0
# # i=2
# # while i<=n:
# #      esum=esum+i
# #      i=i+2
# # print("Sum is",esum)
#
# #sum of odd number and even number using while loop
# #
# # n=int(input("Enter the number"))
# # esum=0
# # osum=0
# # i=1
# # while i<=n:
# #      if i%2== 0:
# #           esum=esum+i
# #      else:
# #           osum=osum+i
# #      i=i+1
# # print("even sum",esum)
# # print("odd sum",osum)
#
# #sum of digits using while loop
#
# # n=int(input("Enter the number"))
# # sum=0
# # while n>0:
# #     i=n%10
# #     sum=sum+i
# #     n=n//10
# # print(sum)
#
# #Find sum of square of digits
#
# # n=int(input("Enter the number"))
# # sum=0
# # while n>0:
# #     i=n%10
# #     sum=sum+i**2
# #     n=n//10
# # print(sum)
#
# #find sum of cube of didgits
#
# # n=int(input("Enter the number"))
# # sum=0
# # while n>0:
# #     i=n%10
# #     sum=sum+i**3
# #     n=n//10
# # print(sum)
#
# # check amstrong of given number
# #
# # n=int(input("Enter the number"))
# # num=n
# # sum=0
# # while n>0:
# #     i=n%10
# #     sum=sum+i**3
# #     n=n//10
# # if sum==num:
# #     print("It is amstrong")
# # else:
# #     print("It is not amstrong")
#
# #count the digits of a number
#
# # n=int(input("Enter the number"))
# # c=0
# # while n>0:
# #     c=c+1
# #     n=n//10
# # print(c)
#
# #Nested loop
#
# # for i in range(1,5):
# #     for j in range(1,5):
# #         print("*",end=" ")
# #     print()
#
# #fibanocci series
# #
# # n=int(input("Enter the number"))
# # f=0
# # s=1
# # for i in range(1,n+1):
# #     print(f,end=" ")
# #     t=f+s
# #     f=s
# #     s=t
#
# #Find hour minute secod of given number
# # n=int(input("Enter the number"))
# # hr=n//3600
# # n=n%3600
# # min=n//60
# # sec=n%60
# # print("Hour",hr,"minute",min,"second",sec)
#
# #Creat an electricity bill
#
# #1 st 100 unit no charge
# #100-200 5rs/unit
# #200 above 10rs/unit
#
# # un=int(input("Enter the unit"))
# # if un<100:
# #     charge=0
# #     print("Amount is",charge)
# # elif un>=100 and un<=200:
# #     charge=un-100*5
# #     print("Amount is",charge)
# # elif un>=200:
# #     charge=500+(un-200)*10
# #     print("Amount is",charge)
# # else:
# #     print("WRONG")
#
# # for i in range(1,5):
# #     for j in range(1,5):
# #         print(j,end=" ")
# #     print()
#
#
# # for i in range(1,5):
# #     for j in range(1,i+1):
# #         print(j,end=" ")
# #      print()
#
#
# # n=int(input("Enter the number"))
# # for i in range(0,n):
# #     for j in range(0,n-i-1):
# #         print(end=" ")
# #     for j in range(0,i+1):
# #         print("*",end=" ")
# #     print()
#
#
# # n=int(input("Enter the number"))
# # for i in range(1,n+1):
# #     for j in range(0,(n+1)-i):
# #         print(i,end=" ")
# #     print()
#
#
# # n=int(input("Enter the number"))
# # for i in range(1,n+1):
# #     for j in range(0,(n+1)-i):
# #         print("5",end=" ")
# #     print()
#
#
# # n=int(input("Enter the number"))
# # for i in range(0,n):
# #     for j in range(0,(n+1)-i):
# #         print(j,end=" ")
# #     print()
#
#
# # n=int(input("Enter the number"))
# # for i in range(1,n+1,2):
# #     for j in range(1,i+1,2):
# #         print(i,end=" ")
# #     print()
#
#
# # n=int(input("Enter the number"))
# # for i in range(0,n+1):
# #     for j in range(0,n-i):
# #         k=n-i
# #         print(k,end=" ")
# #     print()
#
#
# # n=int(input("Enter the number"))
# # for i in range(0,n):
# #     for j in range(n-i,0,-1):
# #         print(j,end=" ")
# #     print()
#
# # j="kksfjfo kfjfjoror"
# # print(j.capitalize())
# # print(j.title())
#
# # for i in range(1,11,1):
# #     m=i*7
# #     print(i,"* 7 =",m)
#
# # n=int(input("Enter the number"))
# # for i  in range(1,11,1):
# #     m=i*n
# #     print(i,"*",n,"=",m)
#
# # n= int(input("Enter the number"))
# # f=1
# # for i in range(1,n+1,1):
# #     f=f*i
# # print("factorial of", n ,"is",f)
#
# # n=int(input("Enter the value"))
# # sum=0
# # for i in range(1,n+1,1):
# #     sum=sum+i
# # print("sum of natural number is ",sum)
#
# n=int(input("Enter the number"))
# sum=0
# for i in  range(2,n+1,2):
#     sum=sum+i
# print("Sum of even number is",sum)

# esum=0
# osum=0
# for i in range(1,101,1):
#     if i%2==0:
#         esum=esum+i
#     else:
#         osum=osum+i
# print("Sum of even number is",esum)
# print("Odd sum",osum)

# n=int(input("Enter the number"))
# c=0
# for i in range(1,n+1,1):
#     if n%i==0:
#         c=c+1
#         print(i,end=" ")
# print("\nNumber of factors is",c)


# n=int(input("Enter the number"))
# c=0
# for i in range(1,n+1,1):
#     if n%i==0:
#         c=c+1
# if c==2:
#     print(n,"is a prime number")
# else:
#     print(n,"is not a prime number")

# n=int(input("Enter the number"))
# f=0
# s=1
# for i in range(0,n+1,1):
#     print(f,end=" ")
#     t=f+s
#     f=s
#     s=t

# n=int(input("Enter the number"))
# sum=0
# while n>0:
#     i=n%10
#     sum=sum+i
#     n=n//10
# print(sum)

# str=input("Enter the string")
# c=0
# for i in str:
#     if i in "aeiouAEIOU":
#         c=c+1
# print(c)

# s=input("Enter the string")
# c=1
# for i in s:
#     if i==" ":
#         c=c+1
# print(c)

# s=input("Enter the string")
# c=0
# for i in s:
#     if i==i and i!=" ":
#         c=c+1
# print(c)

# n=int(input("Enter the number"))
# sum=0
# i=2
# while i<=n:
#     sum=sum+i
#     i=i+2
# print(sum)

# n=int(input('Enter the number'))
# esum=0
# osum=0
# i=1
# while i<=n:
#     if i%2==0:
#         esum=esum+i
#     else:
#         osum=osum+i
#     i=i+1
# print(esum)
# print(osum)


# s=input("Enter the string")
# count1=0
# count2=0
# for i in s:
#     if(i.isdigit()):
#         count1=count1+1
#     elif(i.isalpha()):
#         count2=count2+1
# print("Count of digits",count1)
# print("Count of alpha",count2)

#palindrom

# s=input("Enter the string")
# S1=s[::1]
# S2=s[::-1]
# if S1==S2:
#     print("String is palindrom")
# else:
#     print("Not palindrom")

# s="12345a11sdfg11"
# print(s.strip("1"))

# lst=[4,2,5.6,1,9,0,5.6]
# for i in lst:
#     if i==5.6:
#         lst.remove(i)
# print(lst)

# lst=[3,1,7,9,0,4]
# lst.sort(reverse=True)
# print(lst[1])

# OR

# lst=[3,1,7,9,0,4]
# lst.sort()
# print(lst[-2])

# lst=[1,2,2,3,3,3,3,4,4,4,5,5]
# newlst=[]
# for i in lst:
#     if i not in newlst:
#         newlst.append(i)
# print(newlst)

# lst=[1,3,2,5,4,7,9,6]
# elst=[]
# olst=[]
# for i in lst:
#     if i%2==0:
#         elst.append(i)
#     else:
#         olst.append(i)
# print("Even list is",elst)
# print("Odd  list is",olst)

lst=[1,3,2,5,4,7,9,6]
sum=0
for i in lst:
    sum=sum+i
print("sum of given list is",sum)









