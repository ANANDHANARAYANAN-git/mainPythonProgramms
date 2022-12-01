#ASSIGNMENT (11-11-2022)

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

# str=input("Enter the string").split()
# for i in str:
#     if len(i)%2==0:
#         print(i,end=" ")


#5)Find words which are greater than given length

# l=input("Enter the string").split()
# n=int(input("Enter the length"))
# for word in l:
#     if len(word)>n:
#         print(word)

#6)Check a string is symmetrical (str="abab",is symmetrical as both halves of the string are the same).

# s=input("Enter the string")
# lg=len(s)
# if lg%2==0:
#     A=s[:int(lg/2)]
#     B=s[int(lg/2):]
#     if A==B:
#         print("It is symmetrical")
#     else:
#         print("It is not symmetrical")
# else:
#     print("It is not symmetrical")


# def check_sym(string):
#     n=len(string)
#     flag=0
#     if n%2:
#         mid=n//2+1
#     else:
#         mid= n//2
#     start=0
#     end= mid
#     while(start <mid and end<n):
#         if(string[start]== string[end]):
#             end= end+1
#         else:
#             flag=1
#             break
#     if flag==0:
#         print("symmetrical")
#     else:
#         print("not symmetrical")
# s= "abcabc"
# print (s)
# check_sym(s)
# s2= "abcdab"
# print(s2)
# check_sym(s2)


#7)Remove character at even indices of a string

# s=input("Enter the string")
# print("String :",s[1::2])

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

# lst=input("Enter the list").split()
# newlst=list(map(int,lst))
# for i in range(0,len(newlst)-1):
#     for j in range(0,len(newlst)-1):
#         if newlst[i]<newlst[j]:
#             newlst[i],newlst[j]=newlst[j],newlst[i]
# print(newlst)

#12)Count numbers in a list which is greater than a given number
# lst=input("Enter the list").split()
# n=int(input("Enter the number"))
# c=0
# for i in lst:
#     if int(i)>n:
#         c=c+1
# print(c)

#13)Count the number of lowercase and uppercase character in a string

# str=input("Enter the string")
# c1=0
# c2=0
# for i in str:
#     if i.isupper():
#         c1=c1+1
#     else:
#         c2=c2+1
# print("upper count is",c1)
# print("lower count is",c2)

# 14)Let farm={1:'Eeman',2:'Catrine',3:'David'}be a dictionary.
# To add the key value(8:'Jack').
# To display the number of item in dictionary
# To remove the key value pair(2:'Catrine')

# farm={1:'Eeman',2:'Catrine',3:'David'}
# farm[8]='Jack'
# print(farm)
#
# c=0
# for i in farm:
#     c=c+1
# print("Number of item in a list",c)
#
# farm.pop(2)
# print(farm)
#15)Create a tuple  an existing tuple.new tuple contain only the elements divisible by 3

# tup=tuple(input("Enter the number").split())
# print(tup)
# newlst=[]
# for i in tup:
#     if int(i)%3==0:
#         newlst.append(int(i))
# print("New tuple contain elements only divisible by 3",tuple(newlst))





