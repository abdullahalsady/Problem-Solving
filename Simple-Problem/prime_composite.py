number = 16
flag = False
if number == 0 or number == 1:
    print(f"{number} isn't prime number and not composite number.")
elif number > 2:
    for i in range(2, number):
        if number % i == 0:
            flag = True


if flag:
    print(f"{number} is composite number.")
else:
    print(f"{number} is prime number.")
