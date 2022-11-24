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


# lst=[1,2,3,4,5,6,7,8,9]
# n=int(input("Enter the number"))
# for i in lst:
#     if i==n:
#         print("Element found")



# ement=int(input("enter a element"))
# while(low<=upp):
#     mid=(low+upp)//2
#     if element>lst[mid]:
#         low=mid+1
#     elif element<lst[mid]:
#         upp=mid-1
#     elif element==lst[mid]:
#         flag=1
#         break
# if(flag>0):
#     print("element found")
# else:
#     print("element not found")


# str=input("Enter the input").split()
# n=int(input("Enter the limit"))
# c=0
# for i in str:
#     if len(i)>n:
#         c=c+1
# print(c)


#Even tuple and odd tuple creation
# tup=tuple(input("Enter the tup").split())
# print(tup)
# elst=[]
# olst=[]
# for i in tup:
#     if int(i)%2==0:
#         elst.append(int(i))
#     else:
#         olst.append(int(i))
# print("tuple with even numbers:",tuple(elst))
# print("tuple with odd number",tuple(olst))


#cube of digits=amstrong(3digit)

# n=int(input("Enter the number"))
# p=len(str(n))
# print(p)
# num=n
# sum=0
# while n>0:
#     d=n%10
#     sum=sum+d**p
#     n=n//10
# if sum==num:
#     print("It is amstrong")
# else:
#     print("It is not amstrong")

#print prime numbers with in a range
 
# ll=int(input("Enter the upper limt"))
# ul=int(input("Enter the lower limit"))
# for i in range(ll,ul+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         if i!=1:
#             print(i,end=" ")

s=1,2,3,4,5,6
print




















