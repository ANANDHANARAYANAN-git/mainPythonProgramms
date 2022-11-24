#print prime numbers with in a range

ll=int(input("Enter the upper limt"))
ul=int(input("Enter the lower limit"))
for i in range(ll,ul+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        if i!=1:
            print(i,end=" ")
