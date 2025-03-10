# DataTypes In Python

my_str = "my string"
my_int = 123
my_float = 2.34
my_double = 2344.213234566777544
my_bool = True

my_list = [1, 2, 3, 'a', 'b', 'c']
my_tuple = (1, 2, 3, 4, 5)
my_set = {'a', 'b', 'c', 'd', 'a', 'a'}
my_dict = {"key1": "value1", "key2": "value2"}

my_record = {
    "emp_id": 123,
    "emp_name": "Keerthan",
    "salary": 30000,
    "age": 25
}

# print(my_set)
# print(my_record["emp_name"])

# deep dive into DataTypes


# add an item into the list
# my_list.append(100)
# print(my_list)

# delete the last item from the list
# my_list.pop()

# delete an item in any place in the list
# my_list.remove('a')

# insert an item in any place that you want
# my_list.insert(3, 4)

print(my_list.index('b'))

# list slicing
# print(my_list[1:5])

print(my_list[3:])

print(my_list[:4])