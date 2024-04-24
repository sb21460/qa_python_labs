
math_mark = int(input("Please enter Math Marks : "))
english_mark = int(input("Please enter English Marks : "))
ict_mark = int(input("Please enter ICT Marks : "))

mark_list = {"maths": math_mark, "english": english_mark, "ICT": ict_mark}
total_mark = 0
for marks in mark_list.keys():
    if mark_list[marks] > 100 or mark_list[marks] < 0:
        print(f"Invalid {marks} marks entered.")
        mark_list[marks] = int(input("Please enter marks in range between 1 and 100 : "))
    total_mark = total_mark + mark_list[marks]

average_mark = total_mark/3
if average_mark >= 65:
    print("Pass")
else:
    print("Fail")
