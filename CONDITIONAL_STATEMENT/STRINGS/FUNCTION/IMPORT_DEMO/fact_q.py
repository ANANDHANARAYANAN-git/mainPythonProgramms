#create a function for calculating factorial of a number.
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print("factorial",f)
