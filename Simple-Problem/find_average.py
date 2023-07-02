def find_average(a, b, c):
    return (a + b + c) / 3

try:
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    c = float(input("Enter another number: "))
    print(f"The average is: {find_average(a, b, c)}")
except ValueError:
    print("Invalid input. Please enter a floating-point number.")
