try:
    age = int(input("Please enter age in years: "))

except ValueError:
    print("Age is not entered as a valid integer")

if age >= 18:
    print("You are in category A")
elif age >= 16:
    print("You are in category B")
else:
    print("You are in category C")