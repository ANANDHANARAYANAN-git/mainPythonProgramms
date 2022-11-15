str=input("Enter the string").split()
n=int(input("Enter the limit"))
for i in str:
    if len(i)>n:
        print(i)
