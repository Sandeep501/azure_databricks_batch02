num_range = int(input("Enter the range: "))

if num_range < 2:
    print(f"{num_range} is not a prime or its not allowed")
elif num_range == 2:
    print(f"{num_range} is a prime number")
else:
    for i in range(2, num_range+1):
        is_prime = True
        for j in range(2, (i//2)+1):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=" ")
        