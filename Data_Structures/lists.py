# Lists are mutable 

list1 = [1,2,3, 'snoop']
print(list1)


#####     ADD    #####

# Adding data to list using functions append(), insert(), extend()

list1.append((2,0))  # add arguments at the end of list as single element
print(list1)

list1.extend((2,0)) # iterates over its argument and adding each element to the list and extending the list
print(list1)

list1.insert(2, 'JoJo') # insert argument at particular index in list
print(list1)

##### DELETE ######

# del, pop(), remove()

del list1[5]   # del keyword deletes the element from particular index and don't return deleted item
print(list1)

a = list1.pop(1) # pop function return the deleted value
print(list1)
print(a)

list1.remove(1) # remove will delete 1 element
print(list1)
 

###### Access list by slicing #######
#      list[start, end, step] #

print(list1)
print(list1[0:2])     
print(list1[0:2:2])
print(list1[::-1])   # reverse list


######## Sorting ######

list2 = [1, 4, 6, 2, 0, 13]
print(sorted(list2))

list2.sort(reverse=True)
print(list2)

## find out index of a particular element ##
print(list2.index(2))

## Count of a particular element ##
print(list2.count(2))




