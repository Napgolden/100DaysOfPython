def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:   
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")

num = int(input("Type the number to check whether it is a Prime Number:\n"))
prime_checker(num)

