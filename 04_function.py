calculate_to_units = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculate_to_units} {name_of_unit}")


days_to_units(20)
days_to_units(30)
days_to_units(45)
days_to_units(110)
