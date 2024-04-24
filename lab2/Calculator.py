

try:
    value_1 = float(input("Please enter value 1: "))
    value_2 = float(input("Please enter value 2: "))

except ValueError:
    print("Value entered is not a valid number.")

operator = int(input("Please enter "
                 "\n 1 for Addition '+'"
                 "\n 2 for Subtraction '-'"
                 "\n 3 for Multiplication '*'"
                 "\n 4 for Division '/'"
                 "\n 5 for Square 's'\n "))

if operator == 1:
    print(f"{value_1} + {value_2} = {value_1 + value_2}")
elif operator == 2 :
    print(f"{value_1} - {value_2} = {value_1 - value_2}")
elif operator == 3 :
    print(f"{value_1} x {value_2} = {value_1 * value_2}")
elif operator == 4 :
    print(f"{value_1} / {value_2} = {value_1 / value_2}")
elif operator == 5 :
    print(f"{value_1} ^ 2 = {value_1**2}")
    print(f"{value_2} ^ 2 = {value_2**2}")
else :
    print("Invalid value entered")

