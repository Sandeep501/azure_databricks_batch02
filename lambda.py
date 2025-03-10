# def addition(a, b):
#     return a + b

# addition = lambda a, b: f"{a} is greater then {b}" if a > b else f"{a} is smaller then {b}"
# subtraction = lambda a, b: a - b

# print(addition(20, 40))

# map function

# map(param1: function, param2: iterable)

my_nums = [10, 20, 30, 40, 50, 15, 25, 9]

result = list(map(lambda a: a//2, my_nums))
# print(result)

# filter
odd_nums = list(filter(lambda a: a % 2 !=0, my_nums))
# print(odd_nums)

from functools import reduce
# reduce
sum_of_all = reduce(lambda a, b: a+b, my_nums)
print(sum_of_all)



# my_result = []
# for i in my_nums:
#     r = i//2
#     my_result.append(r)
# print(my_result)

