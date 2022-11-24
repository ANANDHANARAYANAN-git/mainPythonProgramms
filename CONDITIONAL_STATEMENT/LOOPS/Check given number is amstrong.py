#amstrong is the sum of cube of digits are eqaal to the number(sum of power of number of digit=number)
n=int(input("Enter the number"))
num=n
sum=0
while n>0:
    d=n%10
    sum=sum+d**3
    n=n//10
if sum==num:
    print("It is amstrong")
else:
    print("It is not amstromg")