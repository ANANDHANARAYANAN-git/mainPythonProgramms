#Binary search(index can't be detected because it is sorted)

#EXAMPLE

##Q1)
# lst=[3,6,32,33,54,89,93,98,99,101]
# key=32
# low=0
# high=9
# mid=low+high/2=0+9/2=4.5=4
# lst[mid]=lst[4]=54>32

# lst[mid]>key#equation
# high=mid-1

# low=0
# high=3
# mid=0+3/2=1.5=1

# lst[mid]<key#equation
# low=mid+1=2

# mid=3+2/2=2
# lst[mid]<key
# low=mid+1=3
# list[mid]=key



# value of mid consider only  integer part.
# value of low index must be always less than or equal to high index only exist.


# #Q2)
# key=34
# low=0
# high=9
# mid=4.5=4
# lst[mid]=lst[4]=54>key
# high=mid-1=3


# low=0
# high=3
# mid=1.5=1
#
# lst[mid]<key
# low=mid+1=2

# low=2
# high=3
# mid=2.5=2
# lst[2]<key
# low=mid+1=3

# low=3
# high=3
# mid=3
# lst[3]<key

# lst[mid]<key
# low=mid+1=4#this case not exist because value of low index always less than or equal to high index is not possible.

# def binary_search(lst,key):
#     low=0
#     high=len(lst)-1
#     while low<=high:
#         mid=(low+high)//2
#         if lst[mid]>key:
#             high=mid-1
#         elif lst[mid]<key:
#             low=mid+1
#         else:
#             print("item found")
#             break
#     else:
#         print("item not found")
# lst=[1,2,3,5]
# key=5
# binary_search(lst,key)



def binary_search(lst,key):
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(low+high)//2  #integer part only taken
        if lst[mid]>key:
            high=mid-1
        elif lst[mid]<key:
            low=mid+1
        else:
            print("item found")
            break
    else:
        print("item not found")
lst=input("Enter the list element").split()
lst=list(map(int,lst))
lst.sort()
key=int(input("Enter the element to be searched"))
binary_search(lst,key)





