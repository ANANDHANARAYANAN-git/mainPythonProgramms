
tup=tuple(input("Enter the tup").split())
print(tup)
elst=[]
olst=[]
for i in tup:
    if int(i)%2==0:
        elst.append(int(i))
    else:
        olst.append(int(i))
print("tuple with even numbers:",tuple(elst))
print("tuple with odd number",tuple(olst))