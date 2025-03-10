# simple challenge
# extrcat 50 odd numbers from a list with out exceeding 2 lines of code

# nums = [50, -----  150]

# output -- [51, 53, 55, 57 ---- 149]

odd_num = []

for i in range(50, 150):
    if i%2 != 0:
        odd_num.append(i)
        
# print(odd_num)
    
    
# list comprehension

# odd_num2 = [i for i in range(50, 150) if i%2 !=0]
# print(odd_num2)

# find out the squares of even numbers from 1, 20 in list

squares_of_even = [i**3 for i in range(1, 21) if i%2 == 0]
print(squares_of_even)
