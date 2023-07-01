def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

try:
    celsius = float(input("Please enter a number: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"The Celsius value {celsius} is equivalent to {fahrenheit} degrees Fahrenheit.")
except ValueError:
    print("Invalid input. Please enter a floating-point number.")
