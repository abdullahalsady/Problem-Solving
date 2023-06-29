def odd_even(number):
    if number == 0:
        print(f"{number} isn't odd number and not even number.")
    elif number % 2 == 0:
        print(f"{number} is even number.")
    else:
        print(f"{number} is odd number.")
    
number = 10
odd_even(number)
