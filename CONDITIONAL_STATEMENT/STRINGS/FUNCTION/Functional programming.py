#Functional programming(4 methode)

#1)lambda function***
#2)map function***
#3)filter function***
#4)list comprehension***


#1)LAMBDA function/anonymous function***(lambda function carrie one value at a time froma list.)

#syntax

#variable_name=lambda arg1,arg2,arg,3......:expression

# sum=lambda a,b:a+b
# print("sum is",sum(3,4))

# or

# sum=lambda a,b:a+b
# s=sum(3,4)
# print("sum is",s)


#Write the lambda function to find square of a number.

# sqrn=lambda a:a*a
# print("square is",sqrn(3))

#Find the average of three numbers using lambda function

# avg=lambda a,b,c:(a+b+c)/3
# print("average is",avg(1,2,3))
#
# or
#
# avg=lambda a,b,c:(a+b+c)/3
# a=int(input("Enter a"))
# b=int(input("Enter b"))
# c=int(input("enter c"))
# print("average is",avg(a,b,c))

#Find largest among two numbers using lambda

# lrg=lambda a,b:a if a>b else b#value to be print at the begining
# print("Large",lrg(5,6))
#
# or
#
# lrg=lambda a,b:max(a,b)
# print("Large",lrg(8,10))

#Find largest amoung three number
# lrg=lambda a,b,c:a if a>=b and a>=c else b if b>=c and b>=a else c
# print("large is",lrg(1,2,3))

#convert a string to uppercase using lambda function

# u=lambda s:s.upper()
# print(u("Hai"))

# or
#
# uppr=lambda s:s.upper()
# st=
# print(u(st))

#2)MAP function(map(fun,lst)),we want to  make same changes in all element***

# def sum(a):
#     return a+ 10
# lst=[1,2,3,4]
# newlst=list(map(sum,lst))
# print(newlst)

# def sum(a):
#     return a*10
# lst=[1,2,3,4]
# newlst=list(map(sum,lst))
# print(newlst)

# def mul(a):
#     return a*a

# lst=[1,2,3,4]
# newlst=list(map(mul,lst))
# print(newlst)

# def mul(a):
#     return a*a
# tup=(1,2,3,4)
# newtup=tuple(map(mul,tup))
# print(newtup)

# lst=input("Enter the number").split()
# new=list(map(int,lst))
# print(new)

#QS) count number of letter in each words by using mapfunction?
# lst=["apple","orange","mango","jackfruit","pineapple"]
# new=list(map(len,lst))
# print(new)

#QS)convert all string into list.
# lst=["one","two","three"]
# new=list(map(list,lst))
# print(new)

#QS)creat a new list that contain cubes of each elements

# def cube(a):
#     return a*a*a
# lst=input("Enter the list elements").split()
# new=list(map(int,lst))
# print(new)
# new1=list(map(cube,new))
# print(new1)

#OR

# lst=input("Enter the number").split()
# newlst=list(map(int,lst))
# new=list(map(lambda a:a**3,newlst))
# print(new)

#QS)create a newlst by subtract 5 from each elements[10,15,20,25]

# lst1=[10,15,20,25]
# new=list(map(lambda a:a-5,lst1))#lambda function carrie one value at a time froma list.
# print(new)

#create a newlst by converting each elements to upper case

# lst=["one","two","three"]
# new=list(map(lambda a:a.upper(),lst))
# print(new)

# list1=[1,2,3,4,5]
# list2=[5,10,15,20]
# new=list(map(lambda x,y:x+y,list1,list2))
# print(new)

#QS)create a new list with the average of corresponding elements of two list
# list1=[1,2,3,4,5]
# list2=[5,10,15,20]
# new=list(map(lambda x,y:(x+y)/2,list1,list2))
# print(new)


#3)filter function(),we want to filter elements from given ***

#syntax

#map(fun,seq or lst)
#filter(fun,seq or lst)

#create a newlist that have the elements>5
# lst=[1,2,3,4,5,6,7,8]
# newlst=list(filter(lambda x:x>5,lst))
# print(newlst)

#create a newlst that have only odd numbers

# lst=[3,1,5,2,6,7]
# newlst=list(filter(lambda a:a%2==1,lst))
# print(newlst)

#create a newlist that have only vowels

# lst=['a','c',"e",'f',"g"]
# newlst=list(filter(lambda x:x in "aeiouAEIOU",lst))
# print(newlst)

#QS)input list elements
#create two list
    #elst-have only even numbers
    #olst-have only odd numbers
#also display the number of elemets in each list.


# lst=input("Enter the number").split()
# lst1=list(map(int,lst))
# lst2=list(filter(lambda a:a%2==0,lst1))
# print(lst2)
# lst3=list(filter(lambda a:a%2==1,lst1))
# print(lst3)
# print("NO.elements in even lst",len(lst2))
# print("NO.elements in odd lst",len(lst3))


#4)lst comprehension(expression first)***(more than one condition ,if  else if  else(model))

# lst=[1,2,3,4,5,6,7,8,9]

# lst=[i+10 for i in range(1,5)]
# print(lst)

# lst1=[1,2,3,4]
# lst2=[a+10 for a in lst1]
# print(lst2)

#creat all element in cap.

# fruit=['apple','oran ge','mango']
# frt=[i.upper() for i in fruit]
# print(frt)

#create a newlist that have number of character in each fruit

# lst=[len(i) for i in fruit]
# print(lst)

# lst=[1,2,3,4,5,6,7,8,9]
# nw=[i for i in lst if i>5]
# print(nw)

#convert all into fruit

# fruit=['apple','orange','mango']
# new=['fruit' for i in fruit]
# print(new)
#find the number of even number less than 100.

# new=[i for i in range(0,100) if i%2==0]
# print(len(new))

#find number of vovel in a string

# str=input('Enter the string')
# new=[i for i in str if i in 'aeiouAEIOU']
# print(len(new))

#create a list have the elements with character 'o'

# nw=[i for i in fruit if 'o' in i]
# print(nw)

#create a newlist from fruit that does not contain orange

# nw=[i for i in fruit if 'orange' not in i]
# print(nw)

#find number of multiple of 7 between 1 and 1000

# nw=[i for i in range(1,1000) if i%7==0]
# print(len(nw))

#list must become all are fruit

# lst=['apple','orange','mango']
# newlst=['fruit' for i in lst]
# print(newlst)

#find the number of even numbers less than 100

# newlst=[i for i in range(1,100) if i%2==0]
# print(len(newlst))

#find number of vowels in a string

# lst=input("Enter the string")
# newlst=[i for i in lst if i in 'aeiouAEIOU']
# print(len(newlst))

#we have to change even position to 'even' and odd position to 'odd'

# lst=[1,2,3,4,5,6,7,8]
# new=['even' if i%2==0 else 'odd' for i in lst]
# print(new)

#replace all the elements as 'flower' except lotus

# lst=['rose','lotus','daisy','sunflower']
# new=['flower' if i!='lotus' else 'lotus' for i in lst]
# print(new)

#replace with 'flower' if element have'o'else with 'fruit'

# lst=['rose','lotus','apple','pinapple']
# newlst=['folwer' if 'o' in i else 'fruit' for i in lst]
# print(newlst)

#replace elements in the given form

lst=[1,2,5,7,10]
new=['<5' if i<5 else '==5'if i==5 else '>5' for i in lst]
print(new)














