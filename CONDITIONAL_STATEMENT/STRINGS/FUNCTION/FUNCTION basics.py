#Function(set of code executed independently,code reusability)

#Syntax

#def function_name():
#     Body of function


#fuction calling

#EG,
# def sum():
#     A=int(input("Enter the number1"))
#     B=int(input("Enter the number2"))
#     C=A+B
#     print(C)
# sum()
# sum()
# sum()
# sum()

# def sum(a,b):
#     c=a+b
#     print("sum is",c)
# sum(5,5)

#substraction
#multiplication
#division

# def sub(a,b):
#     s=a-b
#     print("difference is",s)
# sub(10,5)
#
# def mul(a,b):
#     m=a*b
#     print("product is",m)
# mul(2,5)
#
# def div(a,b):
#     d=a/b
#     print("divisor is",d)
# div(10,2)

# def sum(a,b):#formal arguments/parameters,used in function definition.
#     s=a+b
#     print(s)
# num1=int(input("Enter first number"))#actual arguments/parameters,used in function calling.
# num2=int(input("Enter second number"))#actual arguments/parameters
# sum(num1,num2)

# (when return apply,value of s uses again at the position when the function is called,
# return used to access value of outside the function.)
# def sum(a,b):
#     s=a+b
#     return s
# num1=int(input("Enter first number"))
# num2=int(input("Enter second number"))
# s1=sum(num1,num2)
# avg=s1/2
# print(avg)

# def calc(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return sum,sub,mul,div
# a,b,c,d=calc(3,4)
# print("sum",a)
# print("sub",b)
# print("mul",c)
# print("div",d)

# def calc(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     print(sum,sub,mul,div)
# calc(3,4)

#1)Defult arguments(we can assigne a value when we pass a value),(defult arguments placed after defalt argument)6

# def student_details(r,n,d):
#     print("Roll no",r)
#     print("Name",n)
#     print("Department",d)
# student_details(1,2,3)

# def student_details(r,n,d="5"):
#     print("Roll no",r)
#     print("Name",n)
#     print("Department",d)
# student_details(1,2)

# def student_details(r,n,d="5"):
#     print("Roll no",r)
#     print("Name",n)
#     print("Department",d)
# student_details(1,2,8)


# def student_details(r,n,d="bca",c="STGRG"):#d and c are defult argument,r and n are non defult argument.
#     print("Roll no",r)
#     print("Name",n)
#     print("Department",d)
#     print("college",c)
# student_details(102,"Anu","bcom","HENRY")

#2)Keyword arguments(use former parameter to correct the position,order of function calling is not important)

# def student_details(r,n):
#     print("Roll no",r)
#     print("Name",n)
# student_details(n="adam",r=12)

#3)Variable length arguments(pass any number of argument to a function,add n number of values and executed it,consider as a tuple)
# def var_length(*args):
#     print(type(args))
#     print(args)
#     for i in args:
#         print(i)
# var_length(10,20)
# var_length(1,2,3,4,5,6,7,8,9,10)



