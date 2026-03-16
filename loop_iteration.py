#For loop
x = [1,2,3,4,5,0]
for y in x:
    print(y)   #it means get a number for y which is in x

#break and continue statement
a= [16,7,8,5,3]
for y in a:
    if y == 8:
        print("I found it")
        break #break the line and stop further processing
    print(y)
for y in a:
    if (y == 8):
        print('I got it')
        continue #Continue the other number after getting the value
    print(y)

#loop under loop
nums = [3,4,5,2,4]
for num in nums:
    for letter in "abc":
        print(num, letter )

for x in range(1, 20): #It gives the value from 1 to 1999
    print (x)


#NOW TIME FOR THE WHILE LOOP
x = 0
while x<10:
    x += 1
    print(x)