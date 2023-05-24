import math


# Function to check if a number is a prime number
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# Function to check if a number is breakable
def is_breakable(number):
    if number == 2:
        print("The number is a breakable prime.")
        print("a = 1, b = 1")  # Special case for 2
        return
    if not is_prime(number):
        print("The number is a composite number.")
        return
    if number % 4 == 1:
        print("The number is a breakable prime.")

        sqrt_num = int(math.sqrt(number))  # Find values of a and b
        for a in range(sqrt_num, 1, -1):
            b = number - a * a
            if math.isqrt(b) ** 2 == b:
                print(f"a = {a}, b = {int(math.sqrt(b))}")
                return
    else:
        print("The number is an unbreakable prime.")


num = int(input("Enter a number: "))
is_breakable(num)
