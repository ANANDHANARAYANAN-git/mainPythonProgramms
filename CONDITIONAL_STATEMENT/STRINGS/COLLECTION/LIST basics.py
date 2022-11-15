#list is a collection of hetrogenius data in square bracket,[]
lst=[1,2.3,4,"apple",1,2,2,10]
print(type(lst))
#2.3
#10
#"apple"

print(lst[1])
print(lst[7])
print(lst[3])
print(lst[-7])
print(lst[-1])
print(lst[-5])

lst=[1,2.3,"apple",1,2,2,10]

# list is mutable(To replace)
lst[3]="orange"
print(lst)
lst[6]=10
print(lst)

#slicing
#[2.3,"apple"]
#[2,2,10]

print(lst[1:3])
print(lst[4:])
print(lst[-6:-4])
print(lst[-3:])

print(len(lst))#for length
print(lst.count(1))#for count given number
print(lst.index(1))#to find position ofgiven number

#3 function to add

#append(to add a value in the end of list)
lst.append(9)
print(lst)

#insert(to add a value in any position of list)
lst.insert(2,"orange")
print(lst)
  
#extend(to add more than one elements)
lst.extend([4,5])
print(lst)

#max(to  find maximum value of list)
lst=[4,2,5.6,1,9,0]
print(max(lst))

#min(to find minimum value of list)
print(min(lst))

#sorting(to sort in ascending/descending)

#ascending
lst.sort()
print(lst)


#descending
lst.sort(reverse=True)
print(lst)

#2 function to remove

#pop()  remove last element or given specific element by giving index

lst.pop()
print(lst)

lst.pop(3)
print(lst)

#remove  given element

lst.remove(2)
print(lst)

















