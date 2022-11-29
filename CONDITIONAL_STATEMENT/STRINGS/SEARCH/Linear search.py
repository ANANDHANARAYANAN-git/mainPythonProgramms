#Linear search (each element comparision from left to right)

#syntax linear_search(list,key)


def linear_search(lst,key):
    for i in lst:
        if i==key:
            print("Element found",lst.index(i)+1)
            break
    else:
        print("Element not found")
lst=input("Enter the lsit").split()
lst=list(map(int,lst))
key=int(input("Enter the number"))
