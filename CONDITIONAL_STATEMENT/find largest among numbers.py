#find larget among two numbers
# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# if (num1>num2):
#     print(num1,"largest")
# else:
#     print(num2,"largest")

#largest among three numbers
#a>b,a>c
#b>a,b>c
#c>a,a>b

a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if(a==b and b==c):
    print("all are same")
elif(a>=b and a>=c):
    print(a,"is greater")
elif(b>=a and b>=c):
    print(b,"is greater")
else:
    print(c,"is greater")




