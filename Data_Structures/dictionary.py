## Dictionary holds key value pairs and also mutable

dictionary1 = {1: 'python' , 2: 'nodejs', 3: 'HTML5', 4: 'DOTNET'}
print(dictionary1)

## Adding values

dictionary1[1] = 'javascript'
print(dictionary1)

dictionary1[3] = 'Ruby'
print(dictionary1)

## Deleting values

del dictionary1[1]
print(dictionary1)

dictionary1.pop(2)
print(dictionary1)

print(dictionary1.popitem())
print(dictionary1)

print(dictionary1.keys())
print(dictionary1.values())
