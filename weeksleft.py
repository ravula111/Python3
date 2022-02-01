current_age = input("Enter your age")
max_age = 70
year_week = 52
year_month = 12
year_days = 365
years_left = 90 - int(current_age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
print(
    f"number of years {years_left} number of weeks {weeks_left} number of days {days_left}")
