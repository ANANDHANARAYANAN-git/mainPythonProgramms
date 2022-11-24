# def prm(n):
#     for i in range(2,n):
#         if n%i==0:
#             print(n,"is not a prime number")
#             break
#     else:
#         print(n,"is a prime number")
# prm(8)
# prm(11)

#OR

def prm(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        print(n,"is prime number")
    else:
        print(n,"is not a prime number")
prm(8)
prm(11)