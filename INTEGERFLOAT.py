#Integer
a =10.78
print(a)
#To know the type of variable
print(type(a))

#**********Arithmetic Operators**************
#Addition: 3+2
#subtraction: 3-2
#multiplication: 3*2
#division: 3/2
#floor division: 3//2
#exponentiation: 3**2
#modulus: 3%2
print(3%2) #gives the remainder, modulus operator
#To increment the value of a variable
a += 1 #a = a + 1
print(a)
#Absolute value
print(abs(-5))
#To round a number
print(round(a))


#**********Comparison Operators**************
#Equal to: ==
#Not equal to: !=
#Greater than: >
#Less than: <
#Greater than or equal to: >=
#Less than or equal to: <=
print(3 > 2) 
print(3 < 2) 
b=5
print(a!=b)
print(a > b) 
#convertinng a float to an integer
c=7.9
print(int(c)) #this will give 7, it truncates the decimal part
c='5'
print(int(c)) #this will convert the string '5' to the integer 5