#comment
#print("My name is prasid I am from pipara kapilvastu")
name = "Prasid Bhusal"
print(name)
# To count the length of string: 
print(len(name))
#To get the element from string on specific index:
print(name[2])
#To get the element from string on specific index, first will count the index of the element and last will be n-1 of the index of the element:
print(name[0:6])
#starting and ending with 0
print(name[9:])
#To lower the case of string:
print(name.lower())
#to count the letter in string:
print(name.count("a"))
#to find the character index in string:
print(name.find("prasid"))
#to replace the character in string:
print(name.replace("Prasid","Maya"))
#to concanate the string:
mom="maya"
print(name +', ' +mom + ', ' + 'My name is prasid')
print(f'{name.upper()}, {mom}, WE ARE FAMILY')
#dir functipmn is used to find the function of string:
print(dir(name))
print(dir(mom))
#Help function
print(help(str.lower))
