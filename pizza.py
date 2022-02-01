pizza_size = input("what size pizza you want L M S")
bill = 0
if pizza_size == "L":
    bill += 25
elif pizza_size == "M":
    bill += 15
else:
    bill += 10

extra_cheese = input("do you want extra cheese")
if extra_cheese == "Y":
    bill += 1

extra_peporroni = input("do you want extra pepp")
if extra_peporroni == "Y":
    bill += 2

print(f"total bill = {bill}")
