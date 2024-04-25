ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
ages_length = len(ages)

# # 1
# print(f"Length of the list is {ages_length}")
#
# # 2
# for age in ages:
#     print(age)
#
# # 3
# for x in range(ages_length):
#     ages[x] = ages[x] + 1
#
# print(ages)

# 4
# without deleting
ages1 = [age for age in ages if 16 <= age <= 65]
print(ages1)

# 5
print(f"There are {len(ages1)} people aged between 16 and 65.")

# 6
ages1.sort()
print(f"The sorted list of {len(ages1)} people aged between 16 and 65.\n {ages1}")

# 7

print(f"{(ages_length - len(ages1)) * 100 /ages_length }% of people are aged between 16 and 65.\n {ages1}")
