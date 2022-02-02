import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)
count_members = len(names)
print(count_members)
draw = random.randint(0, count_members)
print(f"Today's bill will be paid by {names[draw]}")
