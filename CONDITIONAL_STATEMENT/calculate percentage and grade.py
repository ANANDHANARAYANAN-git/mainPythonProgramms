#read total mark and calculate percentage,grade
tm=int(input("Enter the total mark"))
p=tm/500*100
print("Percentage",p)
if(p>=80):
    print("A")
elif(p>=60):
    print("B")
elif(p>=50):
    print("C")
elif(p>=40):
    print("D")
else:
    print("Failed")