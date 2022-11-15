#Nested loop
# for i in range(1,6):position of row
#     for j in range(1,4):#colum
#         print("*",end=" ")#4 time eecuted and -
#     print()#-move to the next line

# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()

# i=0
# for i in range(0,5):
#     i=i+1
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# k=0
# for i in range(1,5):
#     for j in range(1,i+1):
#         k=k+1
#         print(k,end=" ")
#     print()


# k=65
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k), end=" ")
#         k=k+1
#     print()

#chr(65)=A,chr(97)=a ,increase by 1
# k=65
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k), end=" ")
#         k=k+1
#     print()

n=int(input("Enter the number"))
for i in range(n):
    for j in range(n-i-1):
        print(end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()








