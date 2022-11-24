#Find factorial of a number using a function

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print("Factorial :",f)
fact(10)