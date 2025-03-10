# # my_dict = {
# #     'key1': 'value1',
# #     'key2': 'value2',
# #     'key3': 'value3'
# # }

# # for k, v in my_dict.items():
# #     print(f"{k} is the key and {v} is the value")
# # for i in range(1, 21, 2):
# #     print(i, end=" ")

# if True:
#     print("Hi")
# elif True:
#     print("Hey")
# elif True:
#     print("Hello")
# else:
#     print("Bye")

# my_status = True
# my_status = False

# print(my_status)


# for i in range(1, 51):
#     if i%2 == 0:
#         print(f"{i} is an even number")

num = int(input())
is_prime = True
for i in range(2, (num//2)+1):
    if num%i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{num} is a prime")
else:
    print(f"{num} is not a prime")

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 
