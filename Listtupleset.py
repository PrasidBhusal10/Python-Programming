course =["name", "age","gender"]
print(course)
#For length
print(len(course))
#To access an element in a list
print(course[0]) #this will give 'name'
print(course[-1])#this will give las element 
print(course[0:2]) #this will give a list with 'name'
#To add an element to the list
course.append("Country")
print(course)
#To add an elemt at a specific position
course.insert(1,"Mom")
print(course)
#To add another list in the list
cour=["work", "hobby"]
course.insert(0,cour) #for specifying the position of the list to be added
print(course)
course.extend(cour) #for general
print(course)
#To remove an element from the list
course.remove("Mom")
print(course)
course.pop() #this will remove the last element
print(course)  
#To reverse the list
course.reverse()    
print(course)  
# #To sort the list
# course.sort() #this  will sort the list in alphabetical order    
print(course)
num=[1,2,3,4,6,5]
num.sort()
print(num)  
#sorting in decending order
num.sort(reverse=True)
print(num)  
x =["mango", "banana", "apple "]
x.sort()
sorted(x) #this will return a new sorted list but will not change the original list
print(x)

#Min and Max AND SUM
print(min(num)) #this will give the minimum value in the list
print(max(num)) #this will give the maximum value in the list
print(sum(num)) #this will give the sum of all the elements in the list
#To find the index of an element in the list
print(x.index("banana")) #this will give the index of 'banana' in the list x    
#To get a true or false value if an element is in the list
print("mango" in x)

#Looping
for items in x:
    print(items)
#To print the item in number of times
for index, items in enumerate(x, start=1):
    print(index, items)

#To join the list into a string
print("!".join(x)) #this will join the list x into a string with a comma as a separator

#Tuples
#Tuples are similar to lists but they are immutable, meaning they cannot be changed after they are created
#They are defined using parentheses () instead of square brackets []
#Tuples are faster than lists because they are immutable
# y=("ram","rom","cpu")
# y[1]="gpu" #this will give an error because tuples are immutable
# print(y)


#Sets
#Sets are unordered collections of unique elements
#They are defined using curly braces {} or the set() function
#Sets are mutable, meaning you can add or remove elements from them
#Sets do not allow duplicate elements
#Sets are useful for removing duplicates from a list or for performing mathematical operations like union, intersection, and difference

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

#To add an element to a set
x.add("orange")
print(x)

#To remove an element from a set
x.remove("banana")
print(x)

#To find the intersection of two sets
print(x.intersection(y))

#To find the union of two sets
print(x.union(y))

#To find the difference of two sets
print(x.difference(y))

#Empty list, tuple and set
empty_list = []
empty_tuple = ()
empty_set = set() #this is the correct way to create an empty set, using {} will create an empty dictionary
print(empty_list)   
print(empty_tuple)
print(empty_set)    