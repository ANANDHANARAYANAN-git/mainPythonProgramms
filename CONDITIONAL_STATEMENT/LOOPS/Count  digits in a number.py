#count digits of a number
n=int(input('Enter the number'))
c=0
while n>0:
    i=n%10
    c=c+1
    n=n//10
print(c)