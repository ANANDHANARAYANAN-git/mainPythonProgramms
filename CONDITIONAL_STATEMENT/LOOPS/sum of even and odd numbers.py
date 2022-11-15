# find sum of even and odd number up to n
n=int(input("Enter the number"))
esum=0
osum=0
for i in range(1,n+1,1):
    if i%2==0:
        esum=esum+i
    else:
        osum=osum+i
print("even sum is",esum)
print("odd sum is",osum)
