#Convert given seconds into the following format x hrs:y mins:z secs
#4600s ,,, 1hr:16mins :66 secs

#coppy from w3 resourse

# t= float(input("Input time in seconds: "))
# while t>0:
#     t= t % (24 * 3600)
#     hr= t// 3600
#     t %= 3600
#     min= t // 60
#     t %= 60
#     sec= t
#     print("h:m:s-> %d:%d:%d" % (hr, min, sec))
#     break


#miss

# n=int(input("Enter the number"))
# hr=n//3600
# n=n%3600
# min=n//60
# s=n%60
# print(hr,"hrs",min,"mins",s,"secs")

#Creat an electricity bill

#1 st 100 unit no charge
#100-200 5rs/unit
#200 above 10rs/unit


# n=int(input("Enter the number"))
# if n<=100:
#     charge=0
#     print("Amount is",charge)
# elif n>100 and n<=200:
#     charge=(n-100)*5
#     print("Amount is",charge)
# else:
#     charge=500+(n-200)*10
#     print("Anount is",charge)

#count number of digits and alphabts.

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

#1)Check a given number is a perfect number or not.

# n=int(input("Enter the number"))
# sum=0
# for i in range (1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print("It  is a perfect number")
# else:
#     print("It is not a perfect number")

#2) * * * * *
#    * * * *
#     * * *
#      * *
#       *

# n=int(input("Enter the number"))
# for i in range(n):
#     for j in range(i):
#         print(end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

#3) A
#   B B
#   C C C
#   D D D D
#   E E E E E

# k=65
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(k),end=" ")
#     k=k+1
#     print()

#4)print only even length word in a given string

#5)Find words which are greater than given length

# l=input("Enter the string").split()
# n=int(input("Enter the length"))
# for word in l:
#     if len(word)==n:
#         print(word)

#6)Check a string is symmetric

#str=input("Enter the string")

#7)Remove character at even indices of a string

# str=input("Enter the string")
# str1=""
# for i in range(len(str)):
#     if i%2==1:
#         str1=str1+str[i]
# print(str1)

#8)Count the number of words in a string

# str=input("Enter the string")
# c=1
# for i in str:
#      if i==" ":
#          c=c+1
# print("Number of words in the string",c)

#9)check given year is leap year or not

# n=int(input("Enter the number"))
# if n%4==0:
#     print(n,"is a leap year")
# else:
#     print(n,"is not a leap year")

#10)multiply all number in a list

# lst=input("Enter the list").split()
# print(lst)
# m=1
# for i in lst:
#     m=m*int(i)
# print("multiple is",m)

#11)sort elements in a list without using built in function sort()

# lst=input("Enter the number").split()
# print(lst)
# newlst=[]
# for i in lst:
#     if i




#12)Count numbers in a list which is greater than a given number
# lst=input("Enter the list").split()
# n=int(input("Enter the number"))
# c=0
# for i in lst:
#     if int(i)>n:
#         c=c+1
# print(c)

#13)Count the number of lowercase and uppercase character in a string

str=input("Enter the string")
c1=0
c2=0
for i in str:
    if i.isupper():
        c1=c1+1
    else:
        c2=c2+1
print(c1)
print(c2)


#even tuple and odd tuple creation





















