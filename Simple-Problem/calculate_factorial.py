def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial
    
number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {calculate_factorial(number)}")
