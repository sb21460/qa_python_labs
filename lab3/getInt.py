min_value = 1
max_value = 100

counter = 0

while counter < 3:
    value = int(input("Please enter any value: "))
    if min_value <= value <= max_value :
        print(f"Entered value {value} is between {min_value} and {max_value}.")
        break
    else:
        counter = counter + 1

if counter > 3:
    print(f"Entered values are not between {min_value} and {max_value}. Maximum tries exceeded.")