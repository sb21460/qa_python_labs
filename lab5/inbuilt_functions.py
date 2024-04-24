import statistics

f = open("data.txt", "r")
data = f.read()

grades = data.split(',')

# converting the strings in list to integer values
# grades_int = []
# for grade in grades:
#     grades_int.append(int(grade)
#
#
# print(f"The minimum value in the list is {min(grades_int)}")
# print(f"The maximum value in the list is {max(grades_int)}")

# using map function
grades = list(map(int,grades))

print(f"The minimum value in the list is {min(grades)}")
print(f"The maximum value in the list is {max(grades)}")

# Display the average of grades to 2 decimal points.
# Tip: use the sum(), len() and round() functions.

average_grade = sum(grades)/len(grades)

print(f"The average of the list is {round(average_grade, 2)}")

# print(f"The average(mean) of the list using statistics is {statistics.mean(grades)}")
#
# print(f"The median of the list using statistics is {statistics.median(grades)}")

# printing mean and median using String Format method
mean = statistics.mean(grades)
mean_text = "The average(mean) of the list using statistics is {fmean:.2f}"

median = statistics.median(grades)
median_text = "The median of the list using statistics is {fmedian:.2f}"

print(mean_text.format(fmean = mean))

print(median_text.format(fmedian = median))

