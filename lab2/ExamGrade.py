# Task 2
marks = int(input("Please enter marks as integer between 1 and 100 : "))

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



