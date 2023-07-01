def fibonacci_sequence(number):
    if number <= 0:
        return []

    fib_seq = [0, 1]
    for i in range(2, number + 1):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])

    return fib_seq


try:
    number = int(input("Please enter a number: "))
    fibonacci_seq = fibonacci_sequence(number)
    print(f"The Fibonacci sequence up to {number} is: {fibonacci_seq}")
except ValueError:
    print("Invalid input. Please enter an integer.")
