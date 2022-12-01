#Linear search (each element comparision from left to right,it can find index value 0f searched number)

#syntax

# linear_search(list,key)


def linear_search(lst1,key):
    for i in lst1:
        if i==key:
            print("Element found",lst1.index(i))
            break
    else:
         print("Element not found")
lst=input("Enter the list").split()
lst1=list(map(int,lst))
key=int(input("Enter the number"))
linear_search(lst1,key)

























