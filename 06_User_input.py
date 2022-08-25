calculate_to_units = 24
name_of_unit = "seconds"
num_of_days = 3


def days_to_units(num_of_days):
    return num_of_days * calculate_to_units


days_to_units(1)
my_var = days_to_units(2)
print(f"{my_var}")
user_input = input("enter number of days it will be converted to seconds \n")
print(f"--------------")
print(f"{user_input * 10}")

print(f"-----------------")
user_input_variable = int(user_input)
print(f"user_input value {user_input_variable * 10}")

# print(f"{user_input_variable * 10}")
# my_var = days_to_units(user_input_variable)
# print(f"converted value {my_var}")
