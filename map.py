# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
treasure_point = position.split(", ")
print(treasure_point)
element_in_list = int(treasure_point[1]) - 1
list = int(treasure_point[0]) - 1
print(f"position as per python row {list} position {element_in_list}")
map[int(list)][int(element_in_list)] = 'x'
# print(f"{row1}\n{row2}\n{row3}")
print(map)

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
