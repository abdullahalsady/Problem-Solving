number = 16
flag = False
if number == 0 or number == 1:
    print(f"{number} isn't odd number and not even number.")
elif number > 2:
    for i in range(2, number):
        if number % i == 0:
            flag = True


if flag:
    print(f"{number} is composite number.")
else:
    print(f"{number} is prime number.")