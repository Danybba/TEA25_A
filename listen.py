# age_1 = 16
# age_2 = 23
# age_3 = 42

ages = [16, 23, 42]

ages[1] = 54

ages.append(67)
ages.insert(1, 12)
ages.pop(1)

for age in ages:
    print("Alter:", age)

print(len(ages))

# print("Alter 1:", ages[0])
# print("Alter 2:", ages[1])
# print("Alter 3:", ages[2])

# todos = ["Go to school", "Go to work", "Go to sleep"]

# for todo in todos:
#     print("Todo:", todo)
