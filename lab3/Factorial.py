number = int(input("Please enter any integer: "))
factorial = 1
counter = number

while counter > 0:
    factorial = factorial * counter
    counter = counter - 1


print(f"Factorial of {number} is {factorial}")