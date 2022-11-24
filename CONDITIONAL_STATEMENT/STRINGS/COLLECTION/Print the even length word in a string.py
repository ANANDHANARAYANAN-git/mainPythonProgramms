#print the even length word in a string.

# str=input("Enter the string")
# lst=str.split()
# print(lst)
# for i in lst:
#     if len(i)%2==0:
#         print(i)
#
#OR

str=input("Enter the string").split()
for i in str:
    if len(i)%2==0:
        print(i)