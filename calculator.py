#Python Calaculator

operator = input("Enter an Operator (+ - * /): ")
num1 = float(input("Enter a number : "))
num2 = float(input("Enter a number : "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))

#quiz add a message for user if someone choose wrong operator 
#Hint else statement 
