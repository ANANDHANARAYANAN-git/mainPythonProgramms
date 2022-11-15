# check a given number is
#divisible by 5 and 7
#div by 5 only
#div by 7 only
#not div by 7 and 5

n=int(input("enter the number"))
if (n%5==0) and (n%7==0):
    print("divisible 5 and 7")
elif n%5==0:
    print("divisible by 5 only")
elif n%7==0:
    print("divisible by 7 only")
else:
    print("not divided by 5 and 7")
