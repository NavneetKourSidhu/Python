# empty dictionary
dictionary1 = {}

# dictionary with integer keys
dictionary1 = {1: 'snoop', 2: 'jojo'}

# dictionary with mixed keys
dictionary1 = {'name': 'jojo', 1: [3, 4, 5]}

# using dictionary()
dictionary1 = dict({1: 'snoop' , 2: 'jojo'})

# from sequence having each item as a pair
dictionary1 = dict([(1, 'snoop'), (2, 'jojo')])

#### Accessing elements from dictionary
print(dictionary1[1])
print(dictionary1.get(2))

#### Trying to access keys which doesn't exist

print(dictionary1.get(3))

##### Key error
#print(dictionary1[3])

###### Changing and adding dictionary elements
dictionary1 = {'name': 'snoop', 'age': 4}

# update value
dictionary1['age'] = 3

print(dictionary1)

## Add item 
dictionary1['address'] = 'Sri Ganganagar'
print(dictionary1)

#########################################
## Removing elements from a dictionary ##
#########################################


squares = {1: 1 , 2: 4, 5: 7, 8: 3}

###### pop() remove a particular item
print(squares.pop(8))

####### popitem() removes last item from dictionary
print(squares.popitem())

######## clear() removes all items
print(squares.clear())

######## del  keyword deletes dictionary itself
