# 3 diff casing

# 1. camelCasing - evenNumbers, squaresOfEven

# 2. PascalCasing - EvenNumbers, SquaresOfEven

# 3. snake_casing - even_numbers, squares_of_even_numbers


# def a():
#     def b():
#         return 0
#     return a


def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# add_num = outer_function(10) # x = 10, y = ?
# print(add_num(20))

# print(inner_function(10))

def calculator():
    def add(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mul(a, b):
        return a * b

    return add, sub, mul

addition, subtraction, multiplication = calculator()

print(addition(10, 20))
print(subtraction(20, 10))

print(add(1, 2))


a = 10
b = 20
c = 30

a, b, c = 10, 20, 30