# I am making a simple calculator program 
operator = input("Enter the operator (+ - * /): ")
num1 = float(input("Enter the your first number")) 
num2 = float(input("Enter the second number"))
if operator == "+":
    result = num1+num2
    print(int(result))
elif operator == "-":
    result= num1-num2
    print(round(result))
elif operator == "*":
    result= num1*num2
    print(result)
elif operator == "/":
    result= num1/num2
    print(result)
else:
    print(f'{operator} is a wrong operator')