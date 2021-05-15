# swapping two variables #

#a = 3
#b = 8
#print(a,b)
#a,b = b,a
#print(a,b)

# Multiple variable assignments #

#a,b,c = 1,2.2,'Snoop'
#a,b,*c = [1,2,3,4,5,3,2]
#print(a,b,c)

# Sum of Even numbers in a list #

#a = [1,4,8,10,2,6]
#s = sum([num for num in a if num%2 == 0])
#print(s)

# Deleting multiple Elements from a list

# Deleting aal even
#a = [1,2,3,4,5]
#del a[1::2]
#print(a)

# Creating lists

#list = [i for i in range(0,20)]
#print(list)  

        #OR
#list = list(range(0,5))
#print(list) 

        # list of strings
#list = [("Hello "+i) for i in ['Snoop',"Snoopy"]]
#print(list)

# Set creation

print({x**2 for x in range(10) if x%2 ==0})

