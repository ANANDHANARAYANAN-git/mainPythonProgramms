#Simple calculator
#addition
#subtraction
#multiplication
#division

print("addition=choice1\nsubtraction=choice2\nmutiplication=choice3\ndivision=choise4")
num1=int(input("Enter number 1"))
num2=int(input("Enter number 2"))
c=int(input("choise"))
if c==1:
    sum=num1+num2
    print("sum is",sum)
elif c==2:
    sub=num1-num2
    print("subtraction is",sub)
elif c==3:
    mult=num1*num2
    print("multiplication is",mult)
elif c==4:
    if(num2==0):#NESTED IF
        print("division is not possible")
    else:
        div=num1/num2
        print("division is",div)
else:
    print("ERROR")