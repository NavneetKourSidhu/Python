########## un ordered collection of unique elements ##########
##### sets are mutable #####

set1 = {1, 2, 3 , 4 , 4 }
print(set1)

set1.add(5)
print(set1)

###### union(), intersection(), difference(), symmetric difference()
set2 = {2,5,3,5,3,1,7,8}

print(set1.union(set2))   #all unique values from both sets 
print(set1.intersection(set2))  #common    
print(set1.difference(set2)) # different from set1
print(set1.symmetric_difference(set2)) # different from both sets


