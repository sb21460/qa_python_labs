marks = int(input("Please enter marks as integer between 1 and 100 : "))
student_level = int(input("Please enter student level 1 or 2 : "))

if student_level == 1:
    if 71 <= marks <= 100:
        print("Distinction")
    elif 61 <= marks <= 70:
        print("Merit")
    elif 50 <= marks <= 60:
        print("Pass")
    elif marks < 50:
        print("Fail")
    else:
        print("Marks entered are not in range between 1 and 100.")
elif student_level == 2:
    if 66 <= marks <= 100:
        print("Distinction")
    elif 51 <= marks <= 65:
        print("Merit")
    elif 40 <= marks <= 50:
        print("Pass")
    elif marks < 40:
        print("Fail")
    else:
        print("Marks entered are not in range between 1 and 100.")
else:
    print("Invalid student level entered.")