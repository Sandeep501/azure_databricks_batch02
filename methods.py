# python function/method

# cond = input("Enter the operation: ")
num1 = int(input("Enter a value: "))
num2 = int(input("Enter b value: "))


def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    return a / b

def main(cond, number1, number2):
    if cond == 'a':
        print(addition(number1, number2))
    elif cond == 's':
        print(subtraction(number1, number2))
    elif cond == 'm':
        print(multiply(number1, number2))
    elif cond == 'd':
        print(division(number1, number2))
    else:
        print("Error: please choose the right option")
        

# main(cond, num1, num2)

def multiArthmaticOper(a, b):
    addition = a + b
    sub = a - b
    mul = a * b
    div = a//b
    return f'add: {addition}, sub: {sub}, mul: {mul}, div: {div}'

print(multiArthmaticOper(num1, num2))



    