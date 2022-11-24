#SET(not access through indexing,duplication not permitted,already sorted)
set={1,3,2,6,4,'a',5,6,7,2}
print(set)
print(len(set))

#add()
set.add(78)
print(set)

#to add multiple elements
set.update({9,0})
print(set)

#To remove
set.pop()
print(set)   #remove 1st element

set.remove('a')
print(set)

set.remove(78)
print(set)

#Union
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.union(set2))

#Intersection

print(set1.intersection(set2))

#Difference

print(set1.difference(set2))

print(set2.difference(set1))






















